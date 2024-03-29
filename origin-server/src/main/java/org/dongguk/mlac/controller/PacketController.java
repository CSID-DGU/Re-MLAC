package org.dongguk.mlac.controller;

import lombok.RequiredArgsConstructor;
import org.dongguk.mlac.dto.common.ResponseDto;
import org.dongguk.mlac.dto.request.PacketRequestDto;
import org.dongguk.mlac.service.PacketService;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequiredArgsConstructor
@RequestMapping("/api/v1/packets")
public class PacketController {

    private final PacketService packetService;

    @PostMapping()
    public ResponseDto<?> filter(@RequestBody PacketRequestDto packetRequestDto) {
        packetService.filter(packetRequestDto);
        return ResponseDto.ok(null);
    }
}
