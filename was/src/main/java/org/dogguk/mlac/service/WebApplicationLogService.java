package org.dogguk.mlac.service;

import lombok.RequiredArgsConstructor;
import org.dogguk.mlac.domain.WebApplicationLog;
import org.dogguk.mlac.dto.request.FilterRequestDto;
import org.dogguk.mlac.dto.type.EAttackType;
import org.dogguk.mlac.repository.WebApplicationLogRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

@Service
@RequiredArgsConstructor
public class WebApplicationLogService {
    private final WebApplicationLogRepository webApplicationLogRepository;
    private final DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd'T'HH:mm:ss");

    @Transactional
    public void saveWebApplicationLog(FilterRequestDto filterRequestDto) {
        webApplicationLogRepository.save(
                WebApplicationLog.builder()
                        .attackedAt(LocalDateTime.parse(filterRequestDto.timestamp(), formatter))
                        .attackType(Enum.valueOf(EAttackType.class, filterRequestDto.attackType()))
                        .build());
    }
}
