package org.dongguk.mlac.controller;

import lombok.RequiredArgsConstructor;
import org.dongguk.mlac.dto.common.ResponseDto;
import org.dongguk.mlac.dto.request.AnalysisResultDto;
import org.dongguk.mlac.service.WebServerLogService;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequiredArgsConstructor
public class WebServerLogController {
    private final WebServerLogService webServerLogService;

    @PostMapping("/api/v1/attack-log")
    public ResponseDto<?> saveAttackLog(@RequestBody AnalysisResultDto analysisResultDto){
        webServerLogService.preventAttack(analysisResultDto);
        return ResponseDto.ok("success");
    }
}
