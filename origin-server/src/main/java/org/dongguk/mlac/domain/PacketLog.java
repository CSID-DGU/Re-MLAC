package org.dongguk.mlac.domain;

import jakarta.persistence.*;
import lombok.AccessLevel;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import org.dongguk.mlac.dto.type.ELocation;

import java.time.LocalDateTime;
import java.util.Random;

@Entity
@Getter
@Table(name = "packet_logs")
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class PacketLog {
    @Id
    @Column(name = "id")
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "input_id", nullable = false, updatable = false)
    private Long inputId;

    @Column(name = "defended_location", nullable = false, updatable = false)
    @Enumerated(EnumType.STRING)
    private ELocation defendedLocation;

    @Column(name = "came_in_at", nullable = false, updatable = false)
    private LocalDateTime cameInAt;

    @Column(name = "created_at", nullable = false, updatable = false)
    private LocalDateTime createdAt;

    @Builder
    public PacketLog(
            Long inputId,
            ELocation defendedLocation,
            LocalDateTime cameInAt
    ) {
        this.inputId = inputId == null ? new Random().nextLong(4_931_592L) : inputId;
        this.defendedLocation = defendedLocation;
        this.cameInAt = cameInAt;
        createdAt = LocalDateTime.now();
    }
}
