package org.dongguk.mlac.domain;

import jakarta.persistence.*;
import lombok.AccessLevel;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import org.dongguk.mlac.dto.type.EArea;
import org.hibernate.annotations.DynamicUpdate;

@Entity
@Getter
@Table(name = "users", uniqueConstraints = {
        @UniqueConstraint(columnNames = {"username"})
})
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@DynamicUpdate
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "username", nullable = false, updatable = false)
    private String username;

    @Column(name = "is_blocked", nullable = false)
    private Boolean isBlocked;

    @Column(name = "area", nullable = false, updatable = false)
    @Enumerated(EnumType.STRING)
    private EArea area;

    @Builder
    public User(
            String username,
            Boolean isBlocked,
            EArea area
    ) {
        this.username = username;
        this.isBlocked = isBlocked;
        this.area = area;
    }

    public void updateBlock(Boolean isBlocked){
        this.isBlocked = isBlocked;
    }
}
