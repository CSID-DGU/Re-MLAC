#!/bin/bash
./gradlew clean build -x test
docker buildx build --platform linux/amd64 --load --tag jjuuuunnii/filter-server .
docker push jjuuuunnii/filter-server
