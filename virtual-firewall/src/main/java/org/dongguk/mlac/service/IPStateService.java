package org.dongguk.mlac.service;

import lombok.RequiredArgsConstructor;
import org.dongguk.mlac.domain.IPState;
import org.dongguk.mlac.dto.request.FilterRequestDto;
import org.dongguk.mlac.dto.request.SystemRequestDto;
import org.dongguk.mlac.dto.type.ELogStatus;
import org.dongguk.mlac.dto.type.EOrganizer;
import org.dongguk.mlac.event.CreateIPStateEvent;
import org.dongguk.mlac.event.UpdateIPStateEvent;
import org.dongguk.mlac.exception.CommonException;
import org.dongguk.mlac.exception.ErrorCode;
import org.dongguk.mlac.repository.IPStateRepository;
import org.springframework.context.ApplicationEventPublisher;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
@RequiredArgsConstructor
public class IPStateService {
    private final IPStateRepository ipStateRepository;

    private final ApplicationEventPublisher applicationEventPublisher;

    @Transactional
    public void createOrUpdateIPState(FilterRequestDto requestDto) {
        EOrganizer organizer = EOrganizer.fromEAttack(requestDto.attackType());
        String ip = requestDto.ip();
        Integer port = Integer.parseInt(requestDto.port());

        // Firewall에 해당하지 않는다면 return
        if (!correspondedFirewall(organizer, ip)) {
            return;
        }

        // IPState가 이미 존재한다면 예외 처리
        IPState ipState = ipStateRepository.findByIpAndPort(ip, port).orElseGet(() -> {
            return ipStateRepository.save(IPState.builder()
                    .ip(ip)
                    .port(port)
                    .isBlocked(false).build());
        });

        if (ipState.getIsBlocked()) {
            return;
        } else {
            ipState.updateBlocked(true);
        }

        // Event 전파
        applicationEventPublisher.publishEvent(CreateIPStateEvent.builder()
                .ip(ipState.getIp())
                .port(ipState.getPort())
                .organizer(organizer).build()
        );
    }

    @Deprecated
    @Transactional
    public void updateIPState(String ip, SystemRequestDto requestDto) {
//        // IPState가 없다면 예외 처리
//        IPState ipState = ipStateRepository.findByIp(ip)
//                .orElseThrow(() -> new CommonException(ErrorCode.NOT_FOUND_RESOURCE));
//
//        // 만약 차단 상태가 같다면 무시
//        if (ipState.getIsBlocked() == requestDto.isBlocked()) {
//            return;
//        }
//
//        // IPState 업데이트
//        ipState.updateBlocked(requestDto.isBlocked());
//
//        // Event 전파
//        applicationEventPublisher.publishEvent(UpdateIPStateEvent.builder()
//                .ip(ipState.getIp())
//                .status(ipState.getIsBlocked() ? ELogStatus.BLOCK : ELogStatus.UNBLOCK)
//                .organizer(EOrganizer.OBSERVING_SYSTEM).build()
//        );

        return;
    }

    private Boolean correspondedFirewall(EOrganizer organizer, String ip) {
        return organizer != null && organizer != EOrganizer.BENIGN && ip != null;
    }
}
