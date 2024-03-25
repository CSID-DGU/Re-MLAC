package org.dogguk.mlac.repository;

import org.dogguk.mlac.domain.User;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {
}
