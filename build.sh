#!/bin/bash

# Define variables
DOCKER_IMAGE_NAME="bbertka/sentiment-flask-app:latest"
DOCKER_FILE="Dockerfile"

# Build Docker image
docker build -t $DOCKER_IMAGE_NAME -f $DOCKER_FILE .
