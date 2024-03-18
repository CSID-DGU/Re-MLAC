package org.dongguk.mlac.domain;

import jakarta.persistence.*;
import lombok.AccessLevel;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import org.dongguk.mlac.dto.type.EAttackType;

import java.time.LocalDateTime;

@Getter
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@Entity
@Table(name = "firewall_logs")
public class FirewallLog {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private Long id;

    @Column(name = "ip")
    private String ip;

    @Column(name = "port")
    private String port;

    @Column(name = "attack_type")
    @Enumerated(EnumType.STRING)
    private EAttackType attackType;

    @Column(name = "attacked_at", nullable = false)
    private LocalDateTime attackedAt;

    @Builder
    public FirewallLog(String ip, String port, EAttackType attackType) {
        this.ip = ip;
        this.port = port;
        this.attackType = attackType;
        this.attackedAt = LocalDateTime.now();
    }

    public static FirewallLog createFirewallLong(String ip, String port, EAttackType attackType) {
        return FirewallLog.builder()
                .ip(ip)
                .port(port)
                .attackType(attackType)
                .build();
    }
}
