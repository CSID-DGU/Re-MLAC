package org.dongguk.mlac.domain;

import jakarta.persistence.*;
import lombok.AccessLevel;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import org.dongguk.mlac.dto.type.EAttackType;

import java.time.LocalDateTime;

@Entity
@Getter
@Table(name = "attack")
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class Attack {
    @Id
    @Column(name = "id")
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "ip")
    private String ip;

    @Column(name = "port")
    private String port;

    @Column(name = "attacked_at")
    private LocalDateTime attackedAt;

    @Column(name = "attack_type")
    @Enumerated(EnumType.STRING)
    private EAttackType attackType;

    @Column(name = "result")
    private boolean result;

    @Builder
    public Attack(String ip, String port, EAttackType attackType, boolean result) {
        this.ip = ip;
        this.port = port;
        this.attackType = attackType;
        this.attackedAt = LocalDateTime.now();
        this.result = result;
    }

    public static Attack createAttack(String ip, String port, EAttackType attackType, boolean result) {
        return Attack.builder()
                .ip(ip)
                .port(port)
                .attackType(attackType)
                .result(result)
                .build();
    }

}
