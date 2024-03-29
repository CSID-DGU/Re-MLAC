package org.dongguk.mlac.domain;

import jakarta.persistence.*;
import lombok.AccessLevel;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.util.ArrayList;
import java.util.List;

@Entity
@Getter
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@Table(name = "regexes")
public class Regex {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private Long id;

    @Column(name = "content", nullable = false, updatable = false)
    private String content;

    @OneToMany(mappedBy = "regex", fetch = FetchType.LAZY, cascade = CascadeType.ALL)
    private List<DummyScriptRegex> dummyScriptRegexes = new ArrayList<>();

    @Builder
    public Regex(String content) {
        this.content = content;
    }
}
