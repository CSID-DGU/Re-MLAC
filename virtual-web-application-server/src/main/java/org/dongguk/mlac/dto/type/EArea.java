package org.dongguk.mlac.dto.type;

import lombok.Getter;
import lombok.RequiredArgsConstructor;

@Getter
@RequiredArgsConstructor
public enum EArea {
    OS("OS"),
    WEB("WEB"),

    ;
    private final String value;


    public static EArea fromEOrganizer(EOrganizer organizer) {
        return switch (organizer) {
            case FTP_PATATOR, SSH_PATATOR -> OS;
            case WEB_ATTACK_BRUTE_FORCE -> WEB;
            default -> null;
        };
    }
}
