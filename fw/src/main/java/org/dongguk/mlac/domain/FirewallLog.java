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
@Table(name = "firewall_logs")
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class FirewallLog {
    @Id
    @Column(name = "id")
    @GeneratedValue(strategy = GenerationType.IDENTITY)
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
    public FirewallLog(String ip, String port, LocalDateTime attackedAt, EAttackType attackType) {
        this.ip = ip;
        this.port = port;
        this.attackedAt = attackedAt;
        this.attackType = attackType;
    }
}
