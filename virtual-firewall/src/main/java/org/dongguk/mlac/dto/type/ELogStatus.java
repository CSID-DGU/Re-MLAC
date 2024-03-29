package org.dongguk.mlac.dto.type;

import lombok.Getter;
import lombok.RequiredArgsConstructor;

@Getter
@RequiredArgsConstructor
public enum ELogStatus {
    BLOCK("BLOCK"),
    UNBLOCK("UNBLOCK");

    private final String value;
}
