package org.dogguk.mlac.dto.common;

import lombok.Getter;
import org.dogguk.mlac.exception.ErrorCode;
@Getter
public class ExceptionDto {
    private final Integer code;
    private final String message;
    public ExceptionDto(ErrorCode errorCode){
        this.code = errorCode.getCode();
        this.message = errorCode.getMessage();
    }
    public static ExceptionDto of(ErrorCode errorCode){
        return new ExceptionDto(errorCode);
    }
}