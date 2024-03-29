package org.dongguk.mlac.event;

import lombok.Builder;
import org.dongguk.mlac.dto.type.EOrganizer;

@Builder
public record CreatePipelineEvent(
        String regex,
        EOrganizer organizer
) {
}
