#!/usr/bin/env bash

# ./utils/setup_all.sh
# Initialize or update .env file
touch .env

# Run all setup scripts
bash ./utils/setup_admin.sh
bash ./utils/setup_flask.sh
bash ./utils/setup_misc.sh
bash ./utils/setup_image.sh
bash ./utils/setup_mysql.sh

echo "Setup completed successfully."
