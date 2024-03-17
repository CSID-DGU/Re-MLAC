package org.dongguk.mlac.dto.type;

import lombok.Getter;
import lombok.RequiredArgsConstructor;

@Getter
@RequiredArgsConstructor
public enum EBodyRegex {
    // XSS 공격 regex
    XSS_REGEX("<script>(.*?)</script>|<[^>]*>"),

    // SQL Injection 공격 regex
    SQL_INJECTION_REGEX(".*[\\s]+or[\\s]+.*|.*[\\s]+and[\\s]+.*|.*[\\s]+xor[\\s]+.*|.*[\\s]+not[\\s]+.*|.*[\\s]+union[\\s]+.*|.*[\\s]+select[\\s]+.*|.*[\\s]+insert[\\s]+.*|.*[\\s]+update[\\s]+.*|.*[\\s]+delete[\\s]+.*|.*[\\s]+drop[\\s]+.*|.*[\\s]+create[\\s]+.*|.*[\\s]+alter[\\s]+.*|.*[\\s]+rename[\\s]+.*|.*[\\s]+truncate[\\s]+.*|.*[\\s]+replace[\\s]+.*|.*[\\s]+like[\\s]+.*|.*[\\s]+regexp[\\s]+.*|.*[\\s]+rlike"),
    ;

    private final String regex;
}
