package org.dongguk.mlac.event;

import lombok.Builder;
import org.dongguk.mlac.dto.type.ELogStatus;
import org.dongguk.mlac.dto.type.EOrganizer;

@Builder
public record UpdateIPStateEvent(
        String ip,
        ELogStatus status,
        EOrganizer organizer
) {
}
