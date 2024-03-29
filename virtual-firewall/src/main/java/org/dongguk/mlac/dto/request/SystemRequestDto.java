package org.dongguk.mlac.dto.request;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Builder;

@Builder
public record SystemRequestDto(
        @JsonProperty("is_blocked")
        Boolean isBlocked
) {
}
