#!/bin/bash
docker build -t trustid:latest .
docker tag trustid:latest your_dockerhub_username/trustid:latest
docker push your_dockerhub_username/trustid:latest