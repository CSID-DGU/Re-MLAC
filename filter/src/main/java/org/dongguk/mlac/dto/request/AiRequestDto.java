package org.dongguk.mlac.dto.request;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Builder;

import java.util.List;
import java.util.Map;

public record AiRequestDto(

        String ip,
        String port,
        String timestamp,
        List<Map<String, String>> body,
        @JsonProperty("packet_info")
        Map<String, String> packet_info
) {

    @Builder
    public AiRequestDto(String ip, String port, String timestamp, List<Map<String, String>> body, Map<String, String> packet_info){
        this.ip = ip;
        this.port = port;
        this.timestamp = timestamp;
        this.body = body;
        this.packet_info = packet_info;
    }

    @Override
    public String toString() {
        return "AiRequestDto{" +
                "ip='" + ip + '\'' +
                ", port='" + port + '\'' +
                ", timestamp='" + timestamp + '\'' +
                ", body=" + body +
                ", packet_info=" + packet_info +
                '}';
    }

    public static AiRequestDto of(String ip, String port, String timestamp, List<Map<String, String>> body, Map<String, String> packetInfo) {
        return AiRequestDto.builder()
                .ip(ip)
                .port(port)
                .timestamp(timestamp)
                .body(body)
                .packet_info(packetInfo)
                .build();
    }
}
