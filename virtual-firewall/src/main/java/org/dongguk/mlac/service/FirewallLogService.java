package org.dongguk.mlac.service;

import lombok.RequiredArgsConstructor;
import org.dongguk.mlac.domain.FirewallLog;
import org.dongguk.mlac.dto.type.ELogStatus;
import org.dongguk.mlac.event.CreateIPStateEvent;
import org.dongguk.mlac.event.UpdateIPStateEvent;
import org.dongguk.mlac.repository.FirewallLogRepository;
import org.springframework.context.event.EventListener;
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class FirewallLogService {
    private final FirewallLogRepository firewallLogRepository;

    @Async @EventListener
    public void saveFirewallLog(CreateIPStateEvent event) {
        firewallLogRepository.save(FirewallLog.builder()
                .ip(event.ip())
                .port(event.port())
                .status(ELogStatus.BLOCK)
                .organizer(event.organizer()).build()
        );
    }

    @Async @EventListener
    public void saveFirewallLog(UpdateIPStateEvent event) {
        firewallLogRepository.save(FirewallLog.builder()
                .ip(event.ip())
                .status(event.status())
                .organizer(event.organizer()).build()
        );
    }
}
