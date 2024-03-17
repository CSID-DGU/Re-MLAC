package org.dongguk.mlac.service;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import net.minidev.json.JSONObject;
import org.dongguk.mlac.domain.FirewallLog;
import org.dongguk.mlac.dto.request.FilterRequestDto;
import org.dongguk.mlac.dto.response.AiResponseDto;
import org.dongguk.mlac.dto.type.ErrorCode;
import org.dongguk.mlac.exception.CommonException;
import org.dongguk.mlac.repository.FirewallLogRepository;
import org.dongguk.mlac.util.RestClientUtil;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestClient;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Map;
import java.util.Objects;
import java.util.Optional;

@Service
@RequiredArgsConstructor
@Slf4j
public class FirewallLogService {

    private final FirewallLogRepository firewallLogRepository;


    public void filter(FilterRequestDto filterRequestDto) {
        Optional<FirewallLog> firewallLogOptional = firewallLogRepository.findByIpAndPort(filterRequestDto.ip(),
                filterRequestDto.port());

        if (firewallLogOptional.isPresent()) {
            throw new CommonException(ErrorCode.BANNED_BAD_REQUEST);
        }
    }
}