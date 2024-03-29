package org.dongguk.mlac.exception;

import lombok.AllArgsConstructor;
import lombok.Getter;
import org.springframework.http.HttpStatus;

@Getter
@AllArgsConstructor
public enum ErrorCode {
    //400
    WRONG_ENTRY_POINT(40000, HttpStatus.BAD_REQUEST, "잘못된 접근입니다"),
    MISSING_REQUEST_PARAMETER(40001, HttpStatus.BAD_REQUEST, "필수 요청 파라미터가 누락되었습니다."),
    INVALID_PARAMETER_FORMAT(40002, HttpStatus.BAD_REQUEST, "요청에 유효하지 않은 인자 형식입니다."),
    BAD_REQUEST_JSON(40003, HttpStatus.BAD_REQUEST, "잘못된 JSON 형식입니다."),
    ALREADY_UPDATED(40004, HttpStatus.BAD_REQUEST, "이미 업데이트된 상태입니다."),
    DUPLICATE_RESOURCE(40005, HttpStatus.BAD_REQUEST, "중복된 리소스가 존재합니다."),

    //404
    NOT_FOUND_RESOURCE(40400, HttpStatus.NOT_FOUND, "해당 리소스를 찾을 수 없습니다."),

    //500
    INTERNAL_SERVER_ERROR(50000, HttpStatus.INTERNAL_SERVER_ERROR, "서버 내부 오류입니다")

    ;
    private final Integer code;
    private final HttpStatus httpStatus;
    private final String message;
}
