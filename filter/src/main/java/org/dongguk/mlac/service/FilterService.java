package org.dongguk.mlac.service;
import java.util.regex.Pattern;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import net.minidev.json.JSONObject;
import org.dongguk.mlac.domain.FirewallLog;
import org.dongguk.mlac.domain.Result;
import org.dongguk.mlac.domain.WebServerLog;
import org.dongguk.mlac.dto.request.FilterRequestDto;
import org.dongguk.mlac.dto.response.AiResponseDto;
import org.dongguk.mlac.dto.type.EAttackType;
import org.dongguk.mlac.dto.type.ELocation;
import org.dongguk.mlac.repository.FirewallLogRepository;
import org.dongguk.mlac.repository.ResultRepository;
import org.dongguk.mlac.repository.WebServerLogRepository;
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
    private final DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd'T'HH:mm:ss");

    @Value("${ai-server}")
    private String aiServerUrl;

    @Value("${fw-server}")
    private String fwServerUrl;

    @Value("${web-server}")
    private String webServerUrl;

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

        // TODO: 3. Web Application Server에서 막히는지 확인하는 부분이 필요함


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

        restClientUtil.sendPostRequest(fwServerUrl, aiServerResponse);
        restClientUtil.sendPostRequest(webServerUrl, aiServerResponse);
    }
}