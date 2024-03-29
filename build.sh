#!/bin/bash

# Stop and remove all container
docker compose down
docker rmi re-mlac-input-server
docker rmi re-mlac-origin-server
docker rmi re-mlac-virtual-firewall
docker rmi re-mlac-virtual-web-server
docker rmi re-mlac-virtual-web-application-server

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

cp -r properties/origin/ filter/src/main/resources
cp -r properties/virtual/ fw/src/main/resources
cp -r properties/virtual/ ws/src/main/resources
cp -r properties/virtual/ was/src/main/resources
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
