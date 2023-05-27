#!/usr/bin/env bash

# UFW setup - MKII

# Allow SSH (port 22) for remote access
sudo ufw allow 22/tcp

# Allow HTTP (port 80) for web traffic
sudo ufw allow 80/tcp

# Allow HTTPS (port 443) for secure web traffic
sudo ufw allow 443/tcp

# Allow MySQL (port 3306) for database access
sudo ufw allow 3306/tcp

# Enable the firewall
sudo ufw enable
