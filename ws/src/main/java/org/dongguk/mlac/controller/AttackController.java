package org.dongguk.mlac.controller;

import lombok.RequiredArgsConstructor;
import org.dongguk.mlac.dto.common.ResponseDto;
import org.dongguk.mlac.service.AttackService;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequiredArgsConstructor
public class AttackController {
    private final AttackService attackService;

    @PostMapping("/attack-log")
    public ResponseDto<?> saveAttackLog(@RequestBody String attackLog){
        return ResponseDto.ok(null);
    }
}
