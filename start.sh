#!/bin/bash

# Update and install dependencies
sudo apt update && sudo apt install -y docker docker-compose git

# Add current user to docker group
sudo usermod -aG docker $USER

# Reminder for the user
echo "You may need to re-login or restart your system for docker group changes to take effect."

# Check if certificate exists and set CERT_EXISTS
if [ -f "/etc/letsencrypt/live/zerodaypoke.com/fullchain.pem" ]; then
    export CERT_EXISTS=true
else
    export CERT_EXISTS=false
fi

# Copy the .env file
cp digital_cv/.env digital_cv/src/.env

# Change directory to Flask app
cd digital_cv

# Run the initial setup if required
if [ ! -f ".env" ]; then
  bash ./utils/setup_all.sh
fi

docker-compose up -d nginx redis db flask-app

# Wait for a few seconds to make sure everything is initialized
sleep 30

# Conditional execution of Certbot based on CERT_EXISTS
if [ "$CERT_EXISTS" = false ]; then
  # Run certbot to get the certificates
  docker-compose run --rm certbot

  # Switch Nginx to the SSL-enabled configuration
  docker-compose exec nginx ln -sf /etc/nginx/conf.d/nginx_ssl.conf /etc/nginx/conf.d/default.conf

  # Reload Nginx to pick up the new configuration
  docker-compose exec nginx nginx -s reload
fi
