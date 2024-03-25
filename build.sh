#!/bin/bash

# Stop and remove all container
docker compose down
docker rmi re-mlac-input-server
docker rmi re-mlac-filter-server
docker rmi re-mlac-fw-server
docker rmi re-mlac-ws-server
docker rmi re-mlac-was-server

rm -rf filter/src/main/resources
rm -rf fw/src/main/resources
rm -rf ws/src/main/resources
rm -rf was/src/main/resources
rm -rf input/.env

# Make the environment file
mkdir -p filter/src/main/resources
mkdir -p fw/src/main/resources
mkdir -p ws/src/main/resources
mkdir -p was/src/main/resources

cp properties/filter/application.yml filter/src/main/resources
cp properties/fw/application.yml fw/src/main/resources
cp properties/ws/application.yml ws/src/main/resources
cp properties/ws/data.sql ws/src/main/resources
cp properties/was/application.yml was/src/main/resources
cp properties/input/.env input

# Build the project
cd filter
./gradlew clean build -x test
cd ..

cd ws
./gradlew clean build -x test
cd ..

cd fw
./gradlew clean build -x test
cd ..

cd was
./gradlew clean build -x test
cd ..

# Build the docker image and start the container
docker compose up -d
