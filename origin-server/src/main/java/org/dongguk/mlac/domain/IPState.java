package org.dongguk.mlac.domain;

import jakarta.persistence.*;
import lombok.AccessLevel;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import org.hibernate.annotations.DynamicUpdate;

@Entity
@Getter
@Table(name = "ip_states", uniqueConstraints = {
        @UniqueConstraint(
                columnNames = {"ip", "port"},
                name = "uk_ip_port"
        )
})
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@DynamicUpdate
public class IPState {
    @Id
    @Column(name = "id")
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "ip", nullable = false, updatable = false)
    private String ip;

    @Column(name = "port", nullable = false, updatable = false)
    private Integer port;

    @Column(name = "is_blocked", nullable = false)
    private Boolean isBlocked;

    @Builder
    public IPState(
            String ip,
            Integer port,
            Boolean isBlocked
    ) {
        this.ip = ip;
        this.port = port;
        this.isBlocked = isBlocked;
    }
}
