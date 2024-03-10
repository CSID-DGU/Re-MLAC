package org.dongguk.mlac.repository;

import org.dongguk.mlac.domain.Attack;
import org.springframework.data.jpa.repository.JpaRepository;

public interface AttackRepository extends JpaRepository<Attack, Long> {
}
