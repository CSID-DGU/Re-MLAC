package org.dongguk.mlac.service;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import net.minidev.json.JSONObject;
import org.dongguk.mlac.domain.AiServerLog;
import org.dongguk.mlac.dto.request.FilterRequestDto;
import org.dongguk.mlac.dto.response.AiResponseDto;
import org.dongguk.mlac.dto.type.EAttackType;
import org.dongguk.mlac.dto.type.ErrorCode;
import org.dongguk.mlac.exception.CommonException;
import org.dongguk.mlac.repository.AiServerLogRepository;
import org.dongguk.mlac.util.RestClientUtil;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
@Slf4j
public class AiServerLogService {
    private final RestClientUtil restClientUtil;
    private final DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd'T'HH:mm:ss");

    private final AiServerLogRepository aiServerLogRepository;
    @Value("${ai-server}")
    private String aiServerUrl;

    public JSONObject filter(FilterRequestDto filterRequestDto){
        LocalDateTime nowWithoutNanos = LocalDateTime.now().withNano(0);
        JSONObject aiServerRequest = filterRequestDto.toJsonObject(formatter.format(nowWithoutNanos));
        JSONObject aiResponseJson = restClientUtil.sendPostRequest(aiServerUrl, aiServerRequest);

        AiResponseDto aiResponse = AiResponseDto.fromJsonToDto(aiResponseJson);

        if (aiResponse.attack_type().equals(EAttackType.BENIGN.getType())) {
            AiServerLog aiServerLog = AiServerLog.createAiServerLog(aiResponse, false);
            aiServerLogRepository.save(aiServerLog);
        }
        else {
            AiServerLog aiServerLog = AiServerLog.createAiServerLog(aiResponse, true);
            aiServerLogRepository.save(aiServerLog);
            throw new CommonException(ErrorCode.INSECURE_REQUEST);
        }

        return AiResponseDto.fromJsonObject(aiResponseJson);
    }
}
