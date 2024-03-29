package org.dongguk.mlac.dto.request;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Builder;
import net.minidev.json.JSONObject;

@Builder
public record WasRequestDto(

        Long userId,

        String attackType,

        String timestamp
) {

    public static WasRequestDto of(Long userId, String attackType, String timestamp) {
        return WasRequestDto.builder()
                .userId(userId)
                .attackType(attackType)
                .timestamp(timestamp)
                .build();
    }

    public JSONObject toJsonObject() {
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("user_id", userId);
        jsonObject.put("attack_type", attackType);
        jsonObject.put("timestamp", timestamp);
        return jsonObject;
    }

}
