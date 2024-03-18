FROM openjdk:17-slim

WORKDIR /app

ARG JAR_PATH=./build/libs

COPY ${JAR_PATH}/MLAC-0.0.1-SNAPSHOT.jar ./app.jar

CMD ["java","-jar","./app.jar"]