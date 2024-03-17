package org.dongguk.mlac.domain;

import jakarta.persistence.*;
import lombok.AccessLevel;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import org.dongguk.mlac.dto.response.AiResponseDto;
import org.dongguk.mlac.dto.type.EAttackType;

import java.time.LocalDateTime;

@Entity
@Getter
@Table(name = "ai_server_logs")
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class AiServerLog {
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
    public AiServerLog(String ip, String port, EAttackType attackType, boolean result) {
        this.ip = ip;
        this.port = port;
        this.attackType = attackType;
        this.attackedAt = LocalDateTime.now();
        this.result = result;
    }

    public static AiServerLog createAiServerLog(String ip, String port, EAttackType attackType, boolean result) {
        return AiServerLog.builder()
                .ip(ip)
                .port(port)
                .attackType(attackType)
                .result(result)
                .build();
    }

    public static AiServerLog createAiServerLog(AiResponseDto aiResponseDto, boolean result) {
        return AiServerLog.builder()
                .ip(aiResponseDto.ip())
                .port(aiResponseDto.port())
                .attackType(EAttackType.fromString(aiResponseDto.attack_type()))
                .result(result)
                .build();
    }
}
