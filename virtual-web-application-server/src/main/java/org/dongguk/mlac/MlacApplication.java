package org.dongguk.mlac;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableAsync;

@EnableAsync
@SpringBootApplication
public class MlacApplication {

	public static void main(String[] args) {
		SpringApplication.run(MlacApplication.class, args);
	}

}
