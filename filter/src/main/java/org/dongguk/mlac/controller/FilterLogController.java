package org.dongguk.mlac.controller;

import lombok.RequiredArgsConstructor;
import net.minidev.json.JSONObject;
import org.dongguk.mlac.dto.common.ResponseDto;
import org.dongguk.mlac.dto.request.FilterRequestDto;
import org.dongguk.mlac.service.AiServerLogService;
import org.dongguk.mlac.service.FirewallLogService;
import org.dongguk.mlac.service.WebServerLogService;
import org.dongguk.mlac.util.RestClientUtil;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequiredArgsConstructor
public class FilterLogController {

    private final FirewallLogService firewallLogService;
    private final WebServerLogService webServerLogService;
    private final AiServerLogService aiServerLogService;
    private final RestClientUtil restClientUtil;

    @Value("${fw-server}")
    private String fwServerUrl;

    @RequestMapping("/api/v1/filter")
    public ResponseDto<?> filter(@RequestBody FilterRequestDto filterRequestDto) {
        firewallLogService.filter(filterRequestDto);
        webServerLogService.filter(filterRequestDto);
        JSONObject aiResponse = aiServerLogService.filter(filterRequestDto);

        restClientUtil.sendPostRequest(fwServerUrl, aiResponse);
        // TODO: WAS 서버에게 전달하는 로직 추가
        return ResponseDto.ok(null);
    }
}
