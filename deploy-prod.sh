#!/bin/bash

# Stop and remove all container
docker compose -f docker-compose.prod.yml --env-file ./.properties/env/.prod.env down
docker rmi re-mlac-origin-server
docker rmi re-mlac-virtual-firewall
docker rmi re-mlac-virtual-web-server
docker rmi re-mlac-virtual-web-application-server

rm -rf origin-server/src/main/resources
rm -rf virtual-firewall/src/main/resources
rm -rf virtual-web-server/src/main/resources
rm -rf virtual-web-application-server/src/main/resources

# Make the environment file
mkdir -p origin-server/src/main/resources
mkdir -p virtual-firewall/src/main/resources
mkdir -p virtual-web-server/src/main/resources
mkdir -p virtual-web-application-server/src/main/resources

cp -r .properties/origin/ origin-server/src/main/resources
cp -r .properties/virtual/* virtual-firewall/src/main/resources
cp -r .properties/virtual/* virtual-web-server/src/main/resources
cp -r .properties/virtual/* virtual-web-application-server/src/main/resources

# Build the project
cd origin-server
./gradlew clean build -x test
cd ..

cd virtual-firewall
./gradlew clean build -x test
cd ..

cd virtual-web-server
./gradlew clean build -x test
cd ..

cd virtual-web-application-server
./gradlew clean build -x test
cd ..

# Build the docker image and start the container
docker compose -f docker-compose.prod.yml --env-file ./.properties/env/.prod.env up -d
