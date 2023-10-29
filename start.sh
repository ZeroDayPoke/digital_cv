#!/bin/bash

# Update and install dependencies
sudo apt update && sudo apt install -y docker docker-compose git

# Add current user to docker group
sudo usermod -aG docker $USER

# Check if Flask app directory exists, if not, clone it
if [ ! -d "$FLASK_APP_REPO" ]; then
    git clone https://github.com/$GIT_USERNAME/$FLASK_APP_REPO.git
else
    echo "$FLASK_APP_REPO directory already exists. Skipping clone."
fi

# Change directory to Flask app
cd $FLASK_APP_REPO

# Start all services except certbot
docker-compose up -d nginx redis db flask-app

# Wait for a few seconds to make sure everything is initialized
sleep 69

# Run certbot to get the certificates
docker-compose run --rm certbot

# Recreate the Nginx service to now include SSL
docker-compose up -d --force-recreate nginx
