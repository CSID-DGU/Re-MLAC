package org.dongguk.mlac.dto.response;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Builder;
import net.minidev.json.JSONObject;

import java.util.List;
import java.util.Map;

@Builder
public record AiResponseDto(
        String ip,
        String port,
        List<Map<String, String>> body,

        String timestamp,
        @JsonProperty("attack_type")
        String attack_type
) {

        @Override
        public String toString() {
                return "AiResponseDto{" +
                        "ip='" + ip + '\'' +
                        ", port='" + port + '\'' +
                        ", body=" + body +
                        ", timestamp='" + timestamp + '\'' +
                        ", attack_type='" + attack_type + '\'' +
                        '}';
        }

        public JSONObject toJsonObject() {
                JSONObject jsonObject = new JSONObject();
                jsonObject.put("ip", ip);
                jsonObject.put("port", port);
                jsonObject.put("timestamp", timestamp);
                jsonObject.put("body", body);
                jsonObject.put("attack_type", attack_type);
                return jsonObject;
        }

        public static JSONObject fromJsonObject(JSONObject jsonObject) {
                return AiResponseDto.builder()
                        .ip(jsonObject.getAsString("ip"))
                        .port(jsonObject.getAsString("port"))
                        .body((List<Map<String, String>>) jsonObject.get("body"))
                        .timestamp(jsonObject.getAsString("timestamp"))
                        .attack_type(jsonObject.getAsString("attack_type"))
                        .build()
                        .toJsonObject()
                        ;
        }

        public static AiResponseDto fromJsonToDto(JSONObject jsonObject) {
                return AiResponseDto.builder()
                        .ip(jsonObject.getAsString("ip"))
                        .port(jsonObject.getAsString("port"))
                        .body((List<Map<String, String>>) jsonObject.get("body"))
                        .timestamp(jsonObject.getAsString("timestamp"))
                        .attack_type(jsonObject.getAsString("attack_type"))
                        .build()
                        ;
        }
}
