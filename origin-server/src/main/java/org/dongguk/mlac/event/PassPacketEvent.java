package org.dongguk.mlac.event;

import lombok.Builder;

import java.time.LocalDateTime;

@Builder
public record PassPacketEvent(
        Long inputId,
        LocalDateTime cameInAt
) {
}
