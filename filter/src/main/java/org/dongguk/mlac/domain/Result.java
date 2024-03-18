package org.dongguk.mlac.domain;

import jakarta.persistence.*;
import lombok.AccessLevel;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import org.dongguk.mlac.dto.type.EAttackType;
import org.dongguk.mlac.dto.type.ELocation;

import java.time.LocalDateTime;

@Entity
@Getter
@Table(name = "`result`")
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class Result {
    @Id
    @Column(name = "id")
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "attacked_at", nullable = false)
    private ELocation attackedAt;

    @Column(name = "created_at", nullable = false)
    private LocalDateTime createdAt;

    @Column(name = "isProtected", nullable = false)
    private Boolean isProtected;

    @Column(name = "attack_type", nullable = false)
    @Enumerated(EnumType.STRING)
    private EAttackType attackType;


    @Builder
    public Result(ELocation attackedAt, LocalDateTime createdAt, Boolean isProtected, EAttackType attackType) {
        this.attackedAt = attackedAt;
        this.createdAt = createdAt;
        this.isProtected = isProtected;
        this.attackType = attackType;
    }

    public static Result createResult(ELocation attackedAt, LocalDateTime createdAt, Boolean isProtected, EAttackType attackType) {
        return Result.builder()
                .attackedAt(attackedAt)
                .createdAt(createdAt)
                .isProtected(isProtected)
                .attackType(attackType)
                .build();
    }


}
