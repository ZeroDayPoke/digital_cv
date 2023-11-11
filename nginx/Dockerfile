# ./Dockerfile.nginx

# Use the official Nginx image as the base
FROM nginx:latest

# Remove the default Nginx configuration
RUN rm /etc/nginx/conf.d/default.conf

# Copy both custom configuration files from the `nginx` directory into the container
COPY ./nginx_init.conf /etc/nginx/conf.d/nginx_init.conf
COPY ./nginx_ssl.conf /etc/nginx/conf.d/nginx_ssl.conf

# Expose ports (docker-compose will handle the port mapping)
EXPOSE 80 443

# Entry script to choose which configuration to use
COPY ./nginx/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Default command to run when the container starts
CMD ["/entrypoint.sh"]
