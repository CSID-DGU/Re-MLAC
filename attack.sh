#!/bin/bash

count=0

while [ $count -lt 100000 ]
do
   output=$(curl -X GET http://localhost:8000)
   echo "index: $count"
   ((count++))
   sleep 0.005
done
