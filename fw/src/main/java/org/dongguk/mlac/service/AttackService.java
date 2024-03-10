package org.dongguk.mlac.service;

import lombok.RequiredArgsConstructor;
import org.dongguk.mlac.domain.Attack;
import org.dongguk.mlac.dto.AnalysisResultDto;
import org.dongguk.mlac.dto.type.EAttackType;
import org.dongguk.mlac.repository.AttackRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;

@Service
@RequiredArgsConstructor
public class AttackService {
    private final AttackRepository attackRepository;
    @Transactional
    public void saveAttackLog(AnalysisResultDto analysisResultDto){
        attackRepository.save(Attack.builder()
                        .ip(analysisResultDto.ip())
                        .port(analysisResultDto.port())
                        .attackedAt(LocalDateTime.now())
                        .attackType(Enum.valueOf(EAttackType.class, analysisResultDto.attackType()))
                .build());
    }
}
