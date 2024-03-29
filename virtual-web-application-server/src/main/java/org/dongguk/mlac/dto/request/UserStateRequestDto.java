package org.dongguk.mlac.dto.request;

import com.fasterxml.jackson.annotation.JsonProperty;
import org.dongguk.mlac.dto.type.EAttack;

import java.util.Map;

public record UserStateRequestDto(
        @JsonProperty("attack_type")
        EAttack attackType,

        @JsonProperty("body")
        Map<String, Object> body
) {
}
