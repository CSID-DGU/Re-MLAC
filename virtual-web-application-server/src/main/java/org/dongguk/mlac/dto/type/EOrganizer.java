package org.dongguk.mlac.dto.type;

import lombok.Getter;
import lombok.RequiredArgsConstructor;

import java.util.Arrays;

@Getter
@RequiredArgsConstructor
public enum EOrganizer {
    WEB_ATTACK_BRUTE_FORCE("WEB_ATTACK_BRUTE_FORCE"),
    FTP_PATATOR("FTP_PATATOR"),
    SSH_PATATOR("SSH_PATATOR"),
    OBSERVING_SYSTEM("OBSERVING_SYSTEM"),

    ;

    private final String value;

    public static EOrganizer fromEAttack(EAttack attack) {
        if (attack == null) {
            return OBSERVING_SYSTEM;
        }

        return Arrays.stream(values())
                .filter(organizer -> organizer.value.equals(attack.toString()))
                .findAny()
                .orElse(null);
    }
}
