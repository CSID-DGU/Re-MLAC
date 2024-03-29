package org.dongguk.mlac.repository;

import org.dongguk.mlac.domain.Regex;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface RegexRepository extends JpaRepository<Regex, Long> {
    @Query("SELECT r FROM Regex r JOIN r.dummyScriptRegexes dsr JOIN dsr.dummyScript ds WHERE ds.content = :content")
    List<Regex> findAllByDummyScriptContent(
            @Param("content") String content
    );
}
