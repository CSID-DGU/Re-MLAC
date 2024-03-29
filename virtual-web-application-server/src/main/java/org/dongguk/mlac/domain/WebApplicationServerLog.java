package org.dongguk.mlac.domain;


import jakarta.persistence.*;
import lombok.AccessLevel;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import org.dongguk.mlac.dto.type.EArea;
import org.dongguk.mlac.dto.type.ELogStatus;
import org.dongguk.mlac.dto.type.EOrganizer;

import java.time.LocalDateTime;

@Entity
@Getter
@Table(name = "web_application_server_logs")
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class WebApplicationServerLog {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "username", nullable = false, updatable = false)
    private String username;

    @Column(name = "area", nullable = false, updatable = false)
    @Enumerated(EnumType.STRING)
    private EArea area;

    @Column(name = "status", nullable = false, updatable = false)
    @Enumerated(EnumType.STRING)
    private ELogStatus status;

    @Column(name = "organizer", nullable = false, updatable = false)
    @Enumerated(EnumType.STRING)
    private EOrganizer organizer;

    @Column(name = "created_at", nullable = false, updatable = false)
    private LocalDateTime createdAt;

    @Builder
    public WebApplicationServerLog(
            String username,
            EArea area,
            ELogStatus status,
            EOrganizer organizer
    ) {
        this.username = username;
        this.area = area;
        this.status = status;
        this.organizer = organizer;
        this.createdAt = LocalDateTime.now();
    }
}
