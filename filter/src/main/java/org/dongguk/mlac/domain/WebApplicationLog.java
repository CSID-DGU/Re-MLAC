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
@Table(name = "web_application_logs")
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class WebApplicationLog {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "user_id")
    private Long userId;

    @Column(name = "attack_type")
    @Enumerated(EnumType.STRING)
    private EAttackType attackType;

    @Column(name = "attacked_at", nullable = false)
    private LocalDateTime attackedAt;

    @Builder
    public WebApplicationLog(Long userId, EAttackType attackType, LocalDateTime attackedAt) {
        this.userId = userId;
        this.attackType = attackType;
        this.attackedAt = attackedAt;
    }
}
