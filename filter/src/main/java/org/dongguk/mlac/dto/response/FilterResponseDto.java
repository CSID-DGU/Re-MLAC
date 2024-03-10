package org.dongguk.mlac.dto.response;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Builder;

import java.util.List;
import java.util.Map;

@Builder
public record FilterResponseDto(
        String ip,
        String port,
        List<Map<String, String>> body,

        String timestamp,
        @JsonProperty("packet_info")
        Map<String, String> packetInfo
) {
        public static FilterResponseDto of(String ip, String port, List<Map<String, String>> body, String timestamp, Map<String, String> packetInfo) {
                return FilterResponseDto.builder()
                        .ip(ip)
                        .port(port)
                        .body(body)
                        .timestamp(timestamp)
                        .packetInfo(packetInfo)
                        .build();
        }
}
