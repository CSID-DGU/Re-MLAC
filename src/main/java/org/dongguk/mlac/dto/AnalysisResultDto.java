package org.dongguk.mlac.dto;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Builder;

import java.util.List;
import java.util.Map;
@Builder
public record AnalysisResultDto(
        @JsonProperty("ip")
        String ip,
        @JsonProperty("port")
        String port,
        @JsonProperty("body")
        List<Map<String, String>> body,
        @JsonProperty("attack_type")
        String attackType
) {
}
