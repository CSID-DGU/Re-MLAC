package org.dongguk.mlac.repository;

import org.dongguk.mlac.domain.PacketLog;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface PacketLogRepository extends JpaRepository<PacketLog, Long> {
}
