package org.dongguk.mlac.domain;

import jakarta.persistence.*;
import lombok.AccessLevel;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import org.dongguk.mlac.dto.type.ELogStatus;
import org.dongguk.mlac.dto.type.EOrganizer;

import java.time.LocalDateTime;

@Entity
@Getter
@Table(name = "web_server_logs")
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class WebServerLog {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private Long id;

    @Column(name = "regex", nullable = false, updatable = false)
    private String regex;

    @Column(name = "status", nullable = false, updatable = false)
    @Enumerated(EnumType.STRING)
    private ELogStatus status;

    @Column(name = "organizer", nullable = false, updatable = false)
    @Enumerated(EnumType.STRING)
    private EOrganizer organizer;

    @Column(name = "created_at", nullable = false, updatable = false)
    private LocalDateTime createdAt;

    @Builder
    public WebServerLog(
            String regex,
            ELogStatus status,
            EOrganizer organizer
    ) {
        this.regex = regex;
        this.status = status;
        this.organizer = organizer;
        this.createdAt = LocalDateTime.now();
    }
}