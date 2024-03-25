package org.dogguk.mlac.controller;

import lombok.RequiredArgsConstructor;
import org.dogguk.mlac.dto.common.ResponseDto;
import org.dogguk.mlac.dto.request.FilterRequestDto;
import org.dogguk.mlac.service.WebApplicationLogService;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/v1")
@RequiredArgsConstructor
public class WebApplicationLogController {

    private final WebApplicationLogService webApplicationLogService;

    @PostMapping("/attack-log")
    public ResponseDto<?> saveWebApplicationLog(@RequestBody FilterRequestDto filterRequestDto){
        webApplicationLogService.saveWebApplicationLog(filterRequestDto);
        return ResponseDto.ok(null);
    }

}
