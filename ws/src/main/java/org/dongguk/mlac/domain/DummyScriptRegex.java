package org.dongguk.mlac.domain;

import jakarta.persistence.*;
import lombok.AccessLevel;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Entity
@Getter
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@Table(name = "dummy_script_regexes", uniqueConstraints = {
        @UniqueConstraint(
                columnNames = {"regex_id", "dummy_script_id"},
                name = "dummy_script_regexes_unique_constraint"
        )
})
public class DummyScriptRegex {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private Long id;

    @ManyToOne
    @JoinColumn(name = "regex_id", nullable = false, updatable = false)
    private Regex regex;

    @ManyToOne
    @JoinColumn(name = "dummy_script_id", nullable = false, updatable = false)
    private DummyScript dummyScript;

    @Builder
    public DummyScriptRegex(Regex regex, DummyScript dummyScript) {
        this.regex = regex;
        this.dummyScript = dummyScript;
    }
}
