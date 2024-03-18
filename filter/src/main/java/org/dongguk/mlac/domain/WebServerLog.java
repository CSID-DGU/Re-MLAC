package org.dongguk.mlac.domain;

import jakarta.persistence.*;
import lombok.AccessLevel;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import org.dongguk.mlac.dto.type.EAttackType;

@Getter
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@Entity
@Table(name = "web_server_logs")
public class WebServerLog {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private Long id;

    @Column(name = "regex", nullable = false)
    private String regex;

    @Enumerated(EnumType.STRING)
    @Column(name = "attack_type", nullable = false)
    private EAttackType attackType;
    @Builder
    public WebServerLog(String regex, EAttackType attackType) {
        this.regex = regex;
        this.attackType = attackType;
    }
}
