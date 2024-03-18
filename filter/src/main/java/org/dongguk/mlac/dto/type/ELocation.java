package org.dongguk.mlac.dto.type;

import lombok.Getter;
import lombok.RequiredArgsConstructor;

@Getter
@RequiredArgsConstructor
public enum ELocation {
    FIREWALL("FIREWALL"),
    WEB_SERVER("WEB_SERVER"),
    WEB_APPLICATION_SERVER("WEB_APPLICATION_SERVER"),
    NONE("NONE");
    private final String location;
}
