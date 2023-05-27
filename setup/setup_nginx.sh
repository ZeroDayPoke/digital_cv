#!/usr/bin/env bash
# Nginx setup script for zerodaypoke.com

set -e

# Update system packages
sudo apt update

# Install Nginx
sudo apt install -y nginx

# Install Certbot for Let's Encrypt SSL certificates
sudo apt install -y certbot python3-certbot-nginx

# Remove the default Nginx configuration
sudo rm -f /etc/nginx/sites-enabled/default
sudo rm -f /etc/nginx/sites-available/default

# Define variables for domain and project path
domain="zerodaypoke.com"
project_path="/var/www/zerodaypoke.com"

# Create a new Nginx configuration file
sudo bash -c "cat > /etc/nginx/sites-available/$domain << 'EOL'
server {
    listen 80;
    server_name $domain www.$domain;

    location / {
        proxy_pass http://127.0.0.1:5050;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
    }

    location /static/ {
        alias $project_path/app/static/;
        expires 30d;
        autoindex off;
    }
}
EOL"

# Create a symbolic link to enable the new site configuration
sudo ln -sf /etc/nginx/sites-available/$domain /etc/nginx/sites-enabled/

# Test the Nginx configuration
sudo nginx -t

# Reload the Nginx service to apply the new configuration
sudo systemctl reload nginx

# Obtain and update SSL certificate using Certbot
sudo certbot --nginx -d $domain -d www.$domain --cert-name $domain --key-type rsa --non-interactive --agree-tos -m admin@$domain

# Create project directory if it doesn't exist
if [ ! -d "$project_path/inbound" ]; then
    # Create project directory
    sudo mkdir $project_path/inbound
fi

# Set appropriate permissions for the project directory
sudo chown -R $USER:$USER $project_path

# Clone the project repository
sudo git clone https://github.com/ZeroDayPoke/digital_cv.git $project_path/inbound

# Install project dependencies
sudo apt install -y python3-pip
sudo pip3 install -r $project_path/inbound/requirements.txt

# GGEZ
echo "Setup complete... QuickStart coming soon..."
