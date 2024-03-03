package org.dongguk.mlac.controller;

import lombok.RequiredArgsConstructor;
import org.dongguk.mlac.dto.AnalysisResultDto;
import org.dongguk.mlac.dto.common.ResponseDto;
import org.dongguk.mlac.service.AttackService;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/v1")
@RequiredArgsConstructor
public class AttackController {
    private final AttackService attackService;
    @PostMapping("/attack-log")
    public ResponseDto<?> saveAttackLog(@RequestBody AnalysisResultDto analysisResultDto){
        attackService.saveAttackLog(analysisResultDto);
        return ResponseDto.ok(null);
    }
}
