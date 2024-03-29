package org.dongguk.mlac.service;

import lombok.RequiredArgsConstructor;
import org.dongguk.mlac.domain.PacketLog;
import org.dongguk.mlac.dto.type.ELocation;
import org.dongguk.mlac.event.BlockPacketEvent;
import org.dongguk.mlac.event.PassPacketEvent;
import org.dongguk.mlac.repository.PacketLogRepository;
import org.springframework.context.event.EventListener;
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class PacketLogService {
    private final PacketLogRepository packetLogRepository;

    @Async @EventListener
    public void savePacketLog(PassPacketEvent event) {
        packetLogRepository.save(PacketLog.builder()
                .inputId(event.inputId())
                .defendedLocation(ELocation.NONE)
                .cameInAt(event.cameInAt()).build()
        );
    }

    @Async @EventListener
    public void savePacketLog(BlockPacketEvent event) {
        packetLogRepository.save(PacketLog.builder()
                .inputId(event.inputId())
                .defendedLocation(event.defendedLocation())
                .cameInAt(event.cameInAt()).build()
        );
    }
}
