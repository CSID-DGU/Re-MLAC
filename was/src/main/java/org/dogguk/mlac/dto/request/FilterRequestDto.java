package org.dogguk.mlac.dto.request;

import com.fasterxml.jackson.annotation.JsonProperty;

public record FilterRequestDto(

        @JsonProperty("user_id")
        Long userId,

        @JsonProperty("timestamp")
        String timestamp,

        @JsonProperty("attack_type")
        String attackType
) {
}
