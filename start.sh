#!/bin/bash

# Update and install dependencies
sudo apt update && sudo apt install -y docker docker-compose git

# Add current user to docker group
sudo usermod -aG docker $USER

# Clone the Flask app repo
git clone https://github.com/zerodaypoke/digital_cv

# Copy the .env file
cp .env digital_cv/

# Change directory to Flask app
cd digital_cv

# Start all services except certbot
docker-compose up -d nginx redis db flask-app

# Wait for a few seconds to make sure everything is initialized
sleep 69

# Run certbot to get the certificates
docker-compose run --rm certbot

# Recreate the Nginx service to now include SSL
docker-compose up -d --force-recreate nginx
