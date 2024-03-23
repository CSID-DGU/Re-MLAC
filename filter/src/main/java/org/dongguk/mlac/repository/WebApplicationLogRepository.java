package org.dongguk.mlac.repository;

import org.dongguk.mlac.domain.WebApplicationLog;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface WebApplicationLogRepository extends JpaRepository<WebApplicationLog, Long> {
}
