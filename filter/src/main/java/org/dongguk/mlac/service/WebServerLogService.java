package org.dongguk.mlac.service;

import java.util.regex.Matcher;
import java.util.regex.Pattern;
import lombok.RequiredArgsConstructor;
import org.dongguk.mlac.domain.WebServerLog;
import org.dongguk.mlac.dto.request.FilterRequestDto;
import org.dongguk.mlac.dto.type.EAttackType;
import org.dongguk.mlac.dto.type.EBodyRegex;
import org.dongguk.mlac.repository.WebServerLogRepository;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class WebServerLogService {
    private final WebServerLogRepository webServerLogRepository;

    private static final Pattern XSS_PATTERN = Pattern.compile(EBodyRegex.XSS_REGEX.getRegex());
    private static final Pattern SQL_INJECTION_PATTERN = Pattern.compile(EBodyRegex.SQL_INJECTION_REGEX.getRegex());


    public void filter(FilterRequestDto filterRequestDto) {
        String body = filterRequestDto.body();
        Matcher XSS_MATCHER = XSS_PATTERN.matcher(body);
        Matcher SQL_INJECTION_MATCHER = SQL_INJECTION_PATTERN.matcher(body);
        // TODO: Heartbleed 취약점 검사 추가

        if (XSS_MATCHER.find()) {
            WebServerLog webServerLog = WebServerLog.createWebServerLog(filterRequestDto, EAttackType.WEB_ATTACK_XSS, true);
            webServerLogRepository.save(webServerLog);
        } else if (SQL_INJECTION_MATCHER.find()) {
            WebServerLog webServerLog = WebServerLog.createWebServerLog(filterRequestDto, EAttackType.WEB_ATTACK_SQL_INJECTION, true);
            webServerLogRepository.save(webServerLog);
        }
        else {
            WebServerLog webServerLog = WebServerLog.createWebServerLog(filterRequestDto, EAttackType.BENIGN, false);
            webServerLogRepository.save(webServerLog);
        }
    }
}
