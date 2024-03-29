package org.dongguk.mlac.repository;

import org.dongguk.mlac.domain.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    Optional<User> findByUsernameAndIsBlocked(String username, Boolean isBlocked);
}
