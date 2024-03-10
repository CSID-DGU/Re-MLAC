package org.dongguk.mlac.exception;

import lombok.Getter;
import lombok.RequiredArgsConstructor;
import org.dongguk.mlac.dto.type.ErrorCode;

@Getter
@RequiredArgsConstructor
public class CommonException extends RuntimeException {
    private final ErrorCode errorCode;

    @Override
    public String getMessage() {
        return errorCode.getMessage();
    }
}
