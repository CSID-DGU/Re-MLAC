package org.dogguk.mlac.domain;

import jakarta.persistence.*;
import lombok.AccessLevel;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Entity
@Getter
@Table(name = "users")
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "is_blocked", nullable = false)
    private Boolean isBlocked;

    @Builder
    public User(Boolean isBlocked) {
        this.isBlocked = isBlocked;
    }
    public void updateBlock(Boolean isBlocked){
        this.isBlocked = isBlocked;
    }
}
