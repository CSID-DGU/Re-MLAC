package org.dongguk.mlac.dto.request;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Builder;
import net.minidev.json.JSONObject;

import java.util.List;
import java.util.Map;

@Builder
public record PacketRequestDto(
        @JsonProperty("ip")
        String ip,

        @JsonProperty("input_id")
        Long inputId,

        @JsonProperty("port")
        String port,

        @JsonProperty("body")
        Map<String, String> body,

        @JsonProperty("packet_info")
        Map<String, String> packetInfo
) {
        public JSONObject toJsonObject(String timestamp) {
                JSONObject jsonObject = new JSONObject();
                jsonObject.put("ip", ip);
                jsonObject.put("port", port);
                jsonObject.put("timestamp", timestamp);
                jsonObject.put("body", body);
                jsonObject.put("packet_info", packetInfo);
                return jsonObject;
        }
}
