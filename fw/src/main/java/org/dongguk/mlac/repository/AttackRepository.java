package org.dongguk.mlac.repository;

import org.dongguk.mlac.domain.FirewallLog;
import org.springframework.data.jpa.repository.JpaRepository;

public interface AttackRepository extends JpaRepository<FirewallLog, Long> {
}
