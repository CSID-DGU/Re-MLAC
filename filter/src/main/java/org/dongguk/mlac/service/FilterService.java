package org.dongguk.mlac.service;
import java.util.List;
import java.util.regex.Pattern;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import net.minidev.json.JSONObject;
import org.dongguk.mlac.domain.*;
import org.dongguk.mlac.dto.request.FilterRequestDto;
import org.dongguk.mlac.dto.request.WasRequestDto;
import org.dongguk.mlac.dto.response.AiResponseDto;
import org.dongguk.mlac.dto.type.EAttackType;
import org.dongguk.mlac.dto.type.ELocation;
import org.dongguk.mlac.dto.type.ErrorCode;
import org.dongguk.mlac.exception.CommonException;
import org.dongguk.mlac.repository.*;
import org.dongguk.mlac.util.RestClientUtil;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Optional;

@Service
@RequiredArgsConstructor
@Slf4j
public class FilterService {

    private final FirewallLogRepository firewallLogRepository;
    private final WebServerLogRepository webServerLogRepository;
    private final ResultRepository resultRepository;
    private final RestClientUtil restClientUtil;
    private final UserRepository userRepository;
    private final DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd'T'HH:mm:ss");

    @Value("${ai-server}")
    private String aiServerUrl;

    @Value("${fw-server}")
    private String fwServerUrl;

    @Value("${web-server}")
    private String webServerUrl;

    @Value("${web-application-server}")
    private String webApplicationServerUrl;

    public void filter(FilterRequestDto filterRequestDto){
        // 1. Firewall에서 막히는지 확인하기
        Optional<FirewallLog> firewallLogOptional = firewallLogRepository.findByIpAndPort(filterRequestDto.ip(), filterRequestDto.port());

        if (firewallLogOptional.isPresent()) {
            resultRepository.save(Result.createResult(ELocation.FIREWALL, LocalDateTime.now(), Boolean.TRUE, firewallLogOptional.get().getAttackType()));
            return;
        }

        // 2. Web Server에서 막히는지 확인
        WebServerLog webServerLog = webServerLogRepository.findAll().stream()
                .filter(log -> Pattern.matches(log.getRegex(), filterRequestDto.body().toString()))
                .findFirst()
                .orElse(null);

        if(webServerLog != null) {
            resultRepository.save(Result.createResult(ELocation.WEB_SERVER, LocalDateTime.now(), Boolean.TRUE, webServerLog.getAttackType()));
            return;
        }

        // 3. Web Application Server에서 막히는지 확인
        Long userId = Long.parseLong(filterRequestDto.body().stream()
                .filter(map -> map.containsKey("user_id"))
                .map(map -> map.get("user_id"))
                .findFirst()
                .orElseThrow(() -> new CommonException(ErrorCode.INVALID_REQUEST_BODY)));

        User user = userRepository.findById(userId).orElseThrow(() -> new CommonException(ErrorCode.NOT_FOUND_USER));

        // 사용자가 차단되어 있는지 확인
        if(user.getIsBlocked()){
            resultRepository.save(Result.createResult(ELocation.WEB_APPLICATION_SERVER, LocalDateTime.now(), Boolean.TRUE, null));
            return;
        }

        // 모든 방어 기법에 막히지 않았으니 AI Server로 요청을 보낸 뒤
        // 반환값에 따라 Log를 기록하고 각 서버로 전파한다.
        LocalDateTime nowWithoutNanos = LocalDateTime.now().withNano(0);
        JSONObject aiServerRequest = filterRequestDto.toJsonObject(formatter.format(nowWithoutNanos));
        JSONObject aiServerResponse = AiResponseDto.fromJsonObject(restClientUtil.sendPostRequest(aiServerUrl, aiServerRequest));

        resultRepository.save(Result.builder()
                .attackedAt(ELocation.NONE)
                .createdAt(nowWithoutNanos)
                .isProtected(Boolean.FALSE)
                .attackType(EAttackType.fromString(aiServerResponse.getAsString("attack_type")))
                .build());

        WasRequestDto wasRequestDto = WasRequestDto.of(userId, aiServerResponse.getAsString("attack_type"), formatter.format(nowWithoutNanos));

        restClientUtil.sendPostRequest(fwServerUrl, aiServerResponse);
        restClientUtil.sendPostRequest(webServerUrl, aiServerResponse);
        restClientUtil.sendPostRequest(webApplicationServerUrl, wasRequestDto.toJsonObject());

        resultRepository.save(Result.createResult(ELocation.NONE, LocalDateTime.now(), Boolean.FALSE, EAttackType.BENIGN));
    }
}