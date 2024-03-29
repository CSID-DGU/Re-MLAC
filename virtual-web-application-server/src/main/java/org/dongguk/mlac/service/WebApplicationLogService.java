package org.dongguk.mlac.service;

import lombok.RequiredArgsConstructor;
import org.dongguk.mlac.domain.WebApplicationServerLog;
import org.dongguk.mlac.event.UpdateUserStateEvent;
import org.dongguk.mlac.repository.WebApplicationLogRepository;
import org.springframework.context.event.EventListener;
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class WebApplicationLogService {
    private final WebApplicationLogRepository webApplicationLogRepository;

    @Async @EventListener
    public void saveWebApplicationServerLog(UpdateUserStateEvent event) {
        webApplicationLogRepository.save(WebApplicationServerLog.builder()
                .username(event.username())
                .status(event.status())
                .area(event.area())
                .organizer(event.organizer()).build()
        );
    }
}
