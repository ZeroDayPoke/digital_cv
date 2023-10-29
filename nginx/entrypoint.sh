# ./nginx/entrypoint.sh

#!/bin/bash

# Check if the SSL certificate exists
if [ -f "/etc/letsencrypt/live/zerodaypoke.com/fullchain.pem" ]; then
    # Symlink to the SSL-enabled configuration
    ln -sf /etc/nginx/conf.d/nginx_ssl.conf /etc/nginx/conf.d/default.conf
else
    # Symlink to the initial configuration
    ln -sf /etc/nginx/conf.d/nginx_init.conf /etc/nginx/conf.d/default.conf
fi

# Start Nginx in foreground
nginx -g "daemon off;"
