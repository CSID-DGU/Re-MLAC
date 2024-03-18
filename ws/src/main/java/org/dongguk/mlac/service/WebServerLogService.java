package org.dongguk.mlac.service;

import lombok.RequiredArgsConstructor;
import org.dongguk.mlac.domain.AttackRegex;
import org.dongguk.mlac.domain.WebServerLog;
import org.dongguk.mlac.dto.request.AnalysisResultDto;
import org.dongguk.mlac.dto.type.EAttackType;
import org.dongguk.mlac.repository.AttackRegexRepository;
import org.dongguk.mlac.repository.WebServerLogRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;
import java.util.regex.Pattern;

@Service
@RequiredArgsConstructor
public class WebServerLogService {
    private final WebServerLogRepository attackRepository;
    private final AttackRegexRepository regexRepository;

    public void preventAttack(AnalysisResultDto analysisResultDto) {
        EAttackType attackType = analysisResultDto.attackType();
        List<AttackRegex> regexes = regexRepository.findAll();

        for (AttackRegex regex : regexes) {
            if (containsAttack(analysisResultDto.body(), regex.getRegex())) {
                if (!attackExists(regex.getRegex())) {
                    saveAttackLog(attackType, regex.getRegex());
                }
            }
        }
    }

    private boolean containsAttack(List<Map<String, String>> bodyList, String regexPattern) {
        for (Map<String, String> body : bodyList) {
            for (String bodyValue: body.values()) {
                if (Pattern.matches(regexPattern, bodyValue)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean attackExists(String regexPattern) {
        return attackRepository.existsByRegex(regexPattern);
    }

    private void saveAttackLog(EAttackType attackType, String regexPattern) {
        attackRepository.save(WebServerLog.createWebServerLog(regexPattern, EAttackType.WEB_ATTACK_SQL_INJECTION));
    }
}
