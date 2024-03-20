package org.dongguk.mlac.service;

import lombok.RequiredArgsConstructor;
import org.dongguk.mlac.domain.FirewallLog;
import org.dongguk.mlac.dto.request.AnalysisResultDto;
import org.dongguk.mlac.dto.type.EAttackType;
import org.dongguk.mlac.repository.AttackRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

@Service
@RequiredArgsConstructor
public class AttackService {
    private final AttackRepository attackRepository;
    private final DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd'T'HH:mm:ss");

    @Transactional
    public void saveAttackLog(AnalysisResultDto analysisResultDto){

        if ("BENIGN".equals(analysisResultDto.attackType())) {
            return ;
        }

        attackRepository.save(FirewallLog.builder()
                        .ip(analysisResultDto.ip())
                        .port(analysisResultDto.port())
                        .attackedAt(LocalDateTime.parse(analysisResultDto.timestamp(), formatter))
                        .attackType(Enum.valueOf(EAttackType.class, analysisResultDto.attackType()))
                .build());
    }
}
