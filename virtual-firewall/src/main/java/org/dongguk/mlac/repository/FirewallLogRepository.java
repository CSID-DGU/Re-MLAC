package org.dongguk.mlac.repository;

import org.dongguk.mlac.domain.FirewallLog;
import org.springframework.data.jpa.repository.JpaRepository;

public interface FirewallLogRepository extends JpaRepository<FirewallLog, Long> {
}
