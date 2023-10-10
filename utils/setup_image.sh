#!/usr/bin/env bash

# ./utils/setup_image.sh

# Function to manage image-related variables in .env
manage_image_env() {
    echo "Setting image-related configurations (press Enter to accept defaults):"

    declare -A image_vars=(
        ["ALLOWED_EXTENSIONS"]="png,jpg,jpeg,gif"
        ["MAX_FILE_SIZE"]="1572864"
        ["UPLOAD_FOLDER"]="app/static/images/"
    )

    for var in "${!image_vars[@]}"; do
        default_value="${image_vars[$var]}"
        read -p "$var [default: $default_value]: " value
        value=${value:-$default_value}
        echo "$var=$value" >>.env
    done
}

manage_image_env
echo "Image configurations set successfully."
