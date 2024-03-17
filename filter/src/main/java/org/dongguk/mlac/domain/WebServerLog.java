package org.dongguk.mlac.domain;

import jakarta.persistence.*;
import lombok.AccessLevel;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import org.dongguk.mlac.dto.request.FilterRequestDto;
import org.dongguk.mlac.dto.type.EAttackType;

import java.time.LocalDateTime;

@Entity
@Getter
@Table(name = "web_server_logs")
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class WebServerLog {
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
    public WebServerLog(String ip, String port, EAttackType attackType, boolean result) {
        this.ip = ip;
        this.port = port;
        this.attackType = attackType;
        this.attackedAt = LocalDateTime.now();
        this.result = result;
    }

    public static WebServerLog createWebServerLog(String ip, String port, EAttackType attackType, boolean result) {
        return WebServerLog.builder()
                .ip(ip)
                .port(port)
                .attackType(attackType)
                .result(result)
                .build();
    }

    public static WebServerLog createWebServerLog(FilterRequestDto filterRequestDto, EAttackType attackType, boolean result) {
        return WebServerLog.builder()
                .ip(filterRequestDto.ip())
                .port(filterRequestDto.port())
                .attackType(attackType)
                .result(result)
                .build();
    }
}
