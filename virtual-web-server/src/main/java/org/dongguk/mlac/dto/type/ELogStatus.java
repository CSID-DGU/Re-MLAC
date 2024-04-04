package org.dongguk.mlac.dto.type;

import lombok.Getter;
import lombok.RequiredArgsConstructor;

@Getter
@RequiredArgsConstructor
public enum ELogStatus {
    CREATE("CREATE"),
    NULL("NULL");

    private final String value;
}
