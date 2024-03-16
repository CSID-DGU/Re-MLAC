package org.dongguk.mlac.batch.config;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.dongguk.mlac.domain.PacketResult;
import org.springframework.batch.core.Job;
import org.springframework.batch.core.Step;
import org.springframework.batch.core.configuration.annotation.EnableBatchProcessing;
import org.springframework.batch.core.configuration.annotation.JobScope;
import org.springframework.batch.core.configuration.annotation.StepScope;
import org.springframework.batch.core.job.builder.JobBuilder;
import org.springframework.batch.core.repository.JobRepository;
import org.springframework.batch.core.step.builder.StepBuilder;
import org.springframework.batch.item.ItemProcessor;
import org.springframework.batch.item.ItemReader;
import org.springframework.batch.item.ItemWriter;
import org.springframework.batch.item.NonTransientResourceException;
import org.springframework.batch.item.ParseException;
import org.springframework.batch.item.UnexpectedInputException;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.transaction.PlatformTransactionManager;

@Slf4j
@Configuration
@RequiredArgsConstructor
@EnableBatchProcessing
public class PacketResultJobConfig {
    private final JobRepository jobRepository;

    @Bean
    public Job packetResultJob(Step packetResultStep) {
        return new JobBuilder("packetResultJob", jobRepository)
                .start(packetResultStep)
                .build();
    }

    @Bean
    @JobScope
    public Step packetResultStep(PlatformTransactionManager transactionManager) {
        return new StepBuilder("packetResultStep", jobRepository)
                .<PacketResult, PacketResult>chunk(10, transactionManager)
                .reader(packetResultItemReader())
                .processor(packetResultItemProcessor())
                .writer(packetResultItemWriter()).build();

    }

    @Bean
    @StepScope
    public ItemReader<PacketResult> packetResultItemReader() {
        return new ItemReader<PacketResult>() {
            @Override
            public PacketResult read()
                    throws Exception, UnexpectedInputException, ParseException, NonTransientResourceException {
                // TODO: data 반환하도록 수정
                return null;
            }
        };
    }

    @Bean
    @StepScope
    public ItemProcessor<PacketResult, PacketResult> packetResultItemProcessor() {
        return item -> item;
    }

    @Bean
    @StepScope
    public ItemWriter<PacketResult> packetResultItemWriter() {
        return items -> {
            for (PacketResult item : items) {
                log.info("Current PacketResult={}", item);
            }
        };
    }
}
