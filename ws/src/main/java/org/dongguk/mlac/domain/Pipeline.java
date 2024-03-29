package org.dongguk.mlac.domain;

import jakarta.persistence.*;
import lombok.AccessLevel;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Entity
@Getter
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@Table(name = "pipelines", uniqueConstraints = {
        @UniqueConstraint(
                columnNames = {"regex"},
                name = "pipelines_unique_constraint"
        )
})
public class Pipeline {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private Long id;

    @Column(name = "regex", nullable = false, updatable = false)
    private String regex;

    @Builder
    public Pipeline(String regex) {
        this.regex = regex;
    }
}
