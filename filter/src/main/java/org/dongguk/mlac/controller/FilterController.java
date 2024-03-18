package org.dongguk.mlac.controller;

import lombok.RequiredArgsConstructor;
import org.dongguk.mlac.dto.common.ResponseDto;
import org.dongguk.mlac.dto.request.FilterRequestDto;
import org.dongguk.mlac.service.FilterService;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequiredArgsConstructor
public class FilterController {

    private final FilterService filterService;

    @RequestMapping("/api/v1/filter")
    public ResponseDto<?> filter(@RequestBody FilterRequestDto filterRequestDto) {
        filterService.filter(filterRequestDto);
        return ResponseDto.ok(null);
    }
}
