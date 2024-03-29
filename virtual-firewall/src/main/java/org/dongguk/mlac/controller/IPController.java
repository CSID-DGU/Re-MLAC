package org.dongguk.mlac.controller;

import lombok.RequiredArgsConstructor;
import org.dongguk.mlac.dto.request.FilterRequestDto;
import org.dongguk.mlac.dto.common.ResponseDto;
import org.dongguk.mlac.dto.request.SystemRequestDto;
import org.dongguk.mlac.service.IPStateService;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/v1/ips")
@RequiredArgsConstructor
public class IPController {
    private final IPStateService ipStateService;

    @PostMapping("")
    public ResponseDto<?> createIPState(
            @RequestBody FilterRequestDto filterRequestDto
    ){
        ipStateService.createOrUpdateIPState(filterRequestDto);
        return ResponseDto.ok(null);
    }

    @PatchMapping("/{ip}")
    public ResponseDto<?> updateIPState(
            @PathVariable("ip") String ip,
            @RequestBody SystemRequestDto systemRequestDto
    ){
        ipStateService.updateIPState(ip, systemRequestDto);
        return ResponseDto.ok(null);
    }
}
