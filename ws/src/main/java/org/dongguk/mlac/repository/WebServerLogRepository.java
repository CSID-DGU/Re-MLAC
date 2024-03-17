package org.dongguk.mlac.repository;

import org.dongguk.mlac.domain.WebServerLog;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

public interface WebServerLogRepository extends JpaRepository<WebServerLog, Long> {

    @Query("select case when count(w) > 0 then true else false end from WebServerLog w where w.regex = :regex")
    boolean existsByRegex(String regex);
}