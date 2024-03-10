package org.dongguk.mlac.dto.request;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Builder;

import java.util.List;
import java.util.Map;

@Builder
public record FilterRequestDto(
        String ip,
        String port,
        List<Map<String, String>> body,
        String attackType,
        @JsonProperty("packet_info")
        Map<String, String> packetInfo
) {
}
