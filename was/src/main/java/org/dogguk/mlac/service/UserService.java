package org.dogguk.mlac.service;

import jakarta.annotation.PostConstruct;
import lombok.RequiredArgsConstructor;
import org.dogguk.mlac.domain.User;
import org.dogguk.mlac.dto.request.FilterRequestDto;
import org.dogguk.mlac.exception.CommonException;
import org.dogguk.mlac.exception.ErrorCode;
import org.dogguk.mlac.repository.UserRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
@RequiredArgsConstructor
public class UserService {
    private final UserRepository userRepository;
    @PostConstruct
    public void createUsers(){
        for(int i=1; i<=1000; i++){
            createTestUser();
        }
    }
    @Transactional
    public void createTestUser(){
        userRepository.save(User.builder()
                .isBlocked(Boolean.FALSE)
                .build()
        );
    }
    public User findById(Long id){
        return userRepository.findById(id)
                .orElseThrow(() -> new CommonException(ErrorCode.NOT_FOUND_USER));
    }
    @Transactional
    public void updateUserBlock(FilterRequestDto filterRequestDto){
        User findUser = findById(filterRequestDto.userId());
        findUser.updateBlock(Boolean.FALSE);
    }
}
