package org.dongguk.mlac.service;

import lombok.RequiredArgsConstructor;
import org.dongguk.mlac.domain.FirewallLog;
import org.dongguk.mlac.dto.request.FilterRequestDto;
import org.dongguk.mlac.dto.response.FilterResponseDto;
import org.dongguk.mlac.dto.type.ErrorCode;
import org.dongguk.mlac.exception.CommonException;
import org.dongguk.mlac.repository.FirewallLogRepository;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.Optional;

@Service
@RequiredArgsConstructor
public class FirewallLogService {

    private final FirewallLogRepository firewallLogRepository;

    public FilterResponseDto filter(FilterRequestDto filterRequestDto) {
        Optional<FirewallLog> firewallLogOptional = firewallLogRepository.findByIpAndPort(filterRequestDto.ip(), filterRequestDto.port());

        if (firewallLogOptional.isPresent()) {
            throw new CommonException(ErrorCode.BANNED_BAD_REQUEST);
        } else {
            return FilterResponseDto.of(
                    filterRequestDto.ip(),
                    filterRequestDto.port(),
                    filterRequestDto.body(),
                    LocalDateTime.now().toString(),
                    filterRequestDto.packetInfo()
            );
        }
    }
}
