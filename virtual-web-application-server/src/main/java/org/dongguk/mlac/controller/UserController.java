package org.dongguk.mlac.controller;

import lombok.RequiredArgsConstructor;
import org.dongguk.mlac.dto.common.ResponseDto;
import org.dongguk.mlac.dto.request.UserStateRequestDto;
import org.dongguk.mlac.service.UserService;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/v1/users")
@RequiredArgsConstructor
public class UserController {
    private final UserService userService;

    @PatchMapping("")
    public ResponseDto<?> updateUserState(
            @RequestBody UserStateRequestDto userStateRequestDto
    ){
        userService.updateUserState(userStateRequestDto);
        return ResponseDto.ok(null);
    }
}
