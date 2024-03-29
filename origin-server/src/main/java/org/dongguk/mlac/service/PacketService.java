package org.dongguk.mlac.service;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import net.minidev.json.JSONObject;
import org.dongguk.mlac.domain.*;
import org.dongguk.mlac.dto.request.PacketRequestDto;
import org.dongguk.mlac.dto.response.AiResponseDto;
import org.dongguk.mlac.dto.type.EAttack;
import org.dongguk.mlac.dto.type.ELocation;
import org.dongguk.mlac.event.BlockPacketEvent;
import org.dongguk.mlac.event.PassPacketEvent;
import org.dongguk.mlac.exception.ErrorCode;
import org.dongguk.mlac.exception.CommonException;
import org.dongguk.mlac.repository.*;
import org.dongguk.mlac.util.RestClientUtil;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.ApplicationEventPublisher;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Optional;

@Service
@RequiredArgsConstructor
@Slf4j
public class PacketService {
    private final IPStateRepository ipStateRepository;
    private final PipelineRepository pipelineRepository;
    private final UserRepository userRepository;

    private final ApplicationEventPublisher applicationEventPublisher;

    private final RestClientUtil restClientUtil;

    private final DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd'T'HH:mm:ss");

    @Value("${analysis-server}")
    private String aiServerUrl;

    @Value("${virtual-firewall}")
    private String fwServerUrl;

    @Value("${virtual-web-server}")
    private String webServerUrl;

    @Value("${virtual-web-application-server}")
    private String webApplicationServerUrl;

    public void filter(PacketRequestDto requestDto){
        Long inputId = requestDto.inputId();
        LocalDateTime now = LocalDateTime.now();

        // 1. Firewall에서 막히는지 확인하기
        Optional<IPState> firewallLogOptional = ipStateRepository.findByIpAndPortAndIsBlocked(
                requestDto.ip(),
                Integer.parseInt(requestDto.port()),
                Boolean.TRUE
        );

        if (firewallLogOptional.isPresent()) {
            applicationEventPublisher.publishEvent(BlockPacketEvent.builder()
                    .inputId(inputId)
                    .defendedLocation(ELocation.FIREWALL)
                    .cameInAt(now)
                    .build());
            return;
        }

        // 2. Web Server에서 막히는지 확인(단, Script가 있는 경우에만 확인)
        Optional<String> script = refineString(requestDto.body(), "script");

        if (script.isPresent()) {
            Pipeline pipeline = pipelineRepository.findAll().stream()
                    .filter(p -> {
                        Pattern pattern = Pattern.compile(p.getRegex(), Pattern.CASE_INSENSITIVE);
                        Matcher matcher = pattern.matcher(script.get());

                        return matcher.find();
                    })
                    .findFirst()
                    .orElse(null);

            if(pipeline != null) {
                applicationEventPublisher.publishEvent(BlockPacketEvent.builder()
                        .inputId(inputId)
                        .defendedLocation(ELocation.WEB_SERVER)
                        .cameInAt(LocalDateTime.now()).build()
                );

                return;
            }
        }

        // 3. Web Application Server에서 막히는지 확인
        Optional<String> username = refineString(requestDto.body(), "username");

        if (username.isPresent()) {
            User user = userRepository.findByUsernameAndIsBlocked(username.get(),  Boolean.TRUE)
                    .orElse(null);

            if(user != null) {
                applicationEventPublisher.publishEvent(BlockPacketEvent.builder()
                        .inputId(inputId)
                        .defendedLocation(ELocation.WEB_APPLICATION_SERVER)
                        .cameInAt(now).build()
                );

                return;
            }
        }

        // 모든 방어 기법에 막히지 않았으니 AI Server로 요청을 보낸 뒤
        // 반환값에 따라 Log를 기록하고 각 서버로 전파한다.
        LocalDateTime nowWithoutNanos = LocalDateTime.now().withNano(0);

        AiResponseDto aiServerResponse = AiResponseDto.fromJsonObject(
                restClientUtil.sendPostRequest(
                        aiServerUrl,
                        requestDto.toJsonObject(formatter.format(nowWithoutNanos))
                )
        );

        if (aiServerResponse.attack_type() != EAttack.BENIGN) {
            aiServerResponse.setIsBlocked(Boolean.TRUE);
            JSONObject virtualRequest = aiServerResponse.toJsonObject();

            restClientUtil.sendPostRequest(fwServerUrl, virtualRequest);
            restClientUtil.sendPostRequest(webServerUrl, virtualRequest);
            restClientUtil.sendPatchRequest(webApplicationServerUrl, virtualRequest);
        }

        applicationEventPublisher.publishEvent(PassPacketEvent.builder()
                .inputId(inputId)
                .cameInAt(now).build()
        );
    }

    private Optional<String> refineString(Map<String, String> map, String key){
        return Optional.ofNullable(map.get(key));
    }
}