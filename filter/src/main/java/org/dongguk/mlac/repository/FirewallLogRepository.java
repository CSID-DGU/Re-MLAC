package org.dongguk.mlac.repository;

import org.dongguk.mlac.domain.FirewallLog;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface FirewallLogRepository extends JpaRepository<FirewallLog, Long> {

    Optional<FirewallLog> findByIpAndPort(String ip, String port);

}
