package org.dongguk.mlac;

import org.springframework.batch.core.configuration.annotation.EnableBatchProcessing;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class MlacApplication {

    public static void main(String[] args) {
        SpringApplication.run(MlacApplication.class, args);
    }

}
