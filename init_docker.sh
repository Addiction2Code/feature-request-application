#!/bin/bash

docker stop serra-feature-handler

docker rm serra-feature-handler

docker build -t serra-feature-handler-img . 

docker run -d --name serra-feature-handler -p 8000:80 serra-feature-handler-img
