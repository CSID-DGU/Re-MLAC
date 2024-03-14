package org.dongguk.mlac.service;

import lombok.RequiredArgsConstructor;
import org.dongguk.mlac.repository.AttackRepository;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class AttackService {
    private final AttackRepository attackRepository;
}
