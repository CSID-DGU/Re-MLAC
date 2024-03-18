package org.dongguk.mlac.dto.type;

import lombok.Getter;
import lombok.RequiredArgsConstructor;
import org.dongguk.mlac.exception.CommonException;

@Getter
@RequiredArgsConstructor
public enum EAttackType {
    BENIGN("BENIGN"),
    PORTSCAN("PORTSCAN"),
    RECONNAISSANCE("RECONNAISSANCE"),
    WEB_ATTACK_BRUTE_FORCE("WEB_ATTACK_BRUTE_FORCE"),
    WEB_ATTACK_XSS("WEB_ATTACK_XSS"),
    WEB_ATTACK_SQL_INJECTION("WEB_ATTACK_SQL_INJECTION"),
    HEARTBLEED("HEARTBLEED"),
    EXPLOITS("EXPLOITS"),
    FUZZERS("FUZZERS"),
    FTP_PATATOR("FTP_PATATOR"),
    SSH_PATATOR("SSH_PATATOR"),
    BACKDOOR("BACKDOOR"),
    BOT("BOT"),
    SHELLCODE("SHELLCODE"),
    WORMS("WORMS"),
    INFILTRATION("INFILTRATION"),
    DOS_SLOWHTTPTEST("DOS_SLOWHTTPTEST"),
    DDOS("DDOS"),
    DOS("DOS"),
    DOS_GOLDENEYE("DOS_GOLDENEYE"),
    DOS_HULK("DOS_HULK"),
    DOS_SLOWLORIS("DOS_SLOWLORIS"),
    GENERIC("GENERIC"),
    ANALYSIS("ANALYSIS");

    private final String type;

    public static EAttackType fromString(String text) {
        for (EAttackType b : EAttackType.values()) {
            if (b.type.equalsIgnoreCase(text)) {
                return b;
            }
        }
        throw new CommonException(ErrorCode.INVALID_ARGUMENT);
    }
}
