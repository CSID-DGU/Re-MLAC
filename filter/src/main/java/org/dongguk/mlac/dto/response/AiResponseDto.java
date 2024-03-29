package org.dongguk.mlac.dto.response;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Builder;
import net.minidev.json.JSONObject;
import org.dongguk.mlac.dto.type.EAttack;

import java.util.Map;

@Builder
public record AiResponseDto(
        @JsonProperty("ip")
        String ip,

        @JsonProperty("port")
        String port,

        @JsonProperty("body")
        Map<String, Object> body,

        @JsonProperty("timestamp")
        String timestamp,

        @JsonProperty("attack_type")
        EAttack attack_type
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

        public void setIsBlocked(Boolean isBlocked) {
                body.put("is_blocked", isBlocked);
        }

        public static AiResponseDto fromJsonObject(JSONObject jsonObject) {
                return AiResponseDto.builder()
                        .ip(jsonObject.getAsString("ip"))
                        .port(jsonObject.getAsString("port"))
                        .body((Map<String, Object>) jsonObject.get("body"))
                        .timestamp(jsonObject.getAsString("timestamp"))
                        .attack_type(EAttack.fromString(jsonObject.getAsString("attack_type"))).build();
        }
}
