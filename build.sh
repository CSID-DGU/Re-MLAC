#!/bin/bash

# Stop and remove all container
docker compose down
docker image prune -a

# Build the project
cd filter
./gradlew clean build -x test
cd ...

cd ws
./gradlew clean build -x test
cd ..

cd fw
./gradlew clean build -x test
cd ..

# Build the docker image and start the container
docker compose up -d