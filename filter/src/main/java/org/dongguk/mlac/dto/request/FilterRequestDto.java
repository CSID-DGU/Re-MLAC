package org.dongguk.mlac.dto.request;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Builder;
import net.minidev.json.JSONObject;

import java.util.List;
import java.util.Map;

@Builder
public record FilterRequestDto(
        String ip,
        String port,
        List<Map<String, String>> body,
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
