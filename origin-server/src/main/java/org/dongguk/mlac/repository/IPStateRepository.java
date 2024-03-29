package org.dongguk.mlac.repository;

import org.dongguk.mlac.domain.IPState;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface IPStateRepository extends JpaRepository<IPState, Long> {
    Optional<IPState> findByIpAndPortAndIsBlocked(String ip, Integer port, Boolean isBlocked);
}
