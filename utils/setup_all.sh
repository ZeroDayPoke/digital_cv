#!/usr/bin/env bash

# ./utils/setup_all.sh
# Initialize or update .env file
touch .env

# Run all setup scripts
bash ./utils/setup_mysql.sh
bash ./utils/setup_admin.sh
bash ./utils/setup_flask.sh

echo "Setup completed successfully."
