package org.dongguk.mlac.dto.request;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Builder;
import org.dongguk.mlac.dto.type.EAttack;

import java.util.Map;

@Builder
public record FilterResultDto(
        @JsonProperty("attack_type")
        EAttack attackType,

        @JsonProperty("body")
        Map<String, String> body
) {
}
