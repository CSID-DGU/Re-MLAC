package org.dongguk.mlac.event;

import lombok.Builder;
import org.dongguk.mlac.dto.type.ELocation;

import java.time.LocalDateTime;

@Builder
public record BlockPacketEvent(
        Long inputId,
        ELocation defendedLocation,
        LocalDateTime cameInAt
) {
}
