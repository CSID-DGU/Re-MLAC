package org.dongguk.mlac.dto.type;

import lombok.Getter;
import lombok.RequiredArgsConstructor;

import java.util.Arrays;

@Getter
@RequiredArgsConstructor
public enum EOrganizer {
    WEB_ATTACK_XSS("WEB_ATTACK_XSS"),
    WEB_ATTACK_SQL_INJECTION("WEB_ATTACK_SQL_INJECTION"),
    EXPLOITS("EXPLOITS"),
    BACKDOOR("BACKDOOR"),
    SHELLCODE("SHELLCODE"),
    INFILTRATION("INFILTRATION"),
    GENERIC("GENERIC"),
    OBSERVING_SYSTEM("OBSERVING_SYSTEM"),

    ;

    private final String value;

    public static EOrganizer fromEAttack(EAttack attack) {
        if (attack == null) {
            return OBSERVING_SYSTEM;
        }

        return Arrays.stream(EOrganizer.values())
                .filter(organizer -> organizer.getValue().equals(attack.toString()))
                .findFirst()
                .orElse(EOrganizer.OBSERVING_SYSTEM);
    }
}