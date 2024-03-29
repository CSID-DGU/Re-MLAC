package org.dongguk.mlac.repository;

import org.dongguk.mlac.domain.WebApplicationServerLog;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface WebApplicationLogRepository extends JpaRepository<WebApplicationServerLog, Long>{
}
