package org.dongguk.mlac.domain;

import jakarta.persistence.*;
import lombok.AccessLevel;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import org.dongguk.mlac.dto.type.EAttackType;

@Entity
@Getter
@Table(name = "web_server_logs")
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class WebServerLog {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private Long id;

    @Column(name = "regex", nullable = false)
    private String regex;

    @Column(name = "attack_type", nullable = false)
    @Enumerated(EnumType.STRING)
    private EAttackType attackType;

    @Builder
    public WebServerLog(String regex, EAttackType attackType) {
        this.attackType = attackType;
        this.regex = regex;
    }

    public static WebServerLog createWebServerLog(String regex, EAttackType attackType) {
        return WebServerLog.builder()
                .regex(regex)
                .attackType(attackType)
                .build();
    }
}