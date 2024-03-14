package org.dongguk.mlac.service;

import lombok.RequiredArgsConstructor;
import org.dongguk.mlac.dto.request.FilterRequestDto;
import org.dongguk.mlac.dto.response.FilterResponseDto;
import org.dongguk.mlac.repository.AttackRepository;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
@RequiredArgsConstructor
public class AttackService {
    private final AttackRepository attackRepository;

    public FilterResponseDto apply(FilterRequestDto filterRequestDto) {
        return FilterResponseDto.of(null, null, null, null, null);
    }
}
