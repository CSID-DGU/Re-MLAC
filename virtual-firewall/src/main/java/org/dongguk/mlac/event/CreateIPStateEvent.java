package org.dongguk.mlac.event;

import lombok.Builder;
import org.dongguk.mlac.dto.type.EOrganizer;

@Builder
public record CreateIPStateEvent(
        String ip,
        Integer port,
        EOrganizer organizer
) {
}
