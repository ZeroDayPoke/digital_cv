#!/usr/bin/env bash

# ./utils/setup_misc.sh

manage_misc_env() {
  misc_vars=("DB_HOST" "FLASK_APP_HOST" "FLASK_APP_PORT" "EMAIL_SERVICE_URL")
  for var in "${misc_vars[@]}"; do
    grep -q "^$var=" .env || {
      read -p "$var: " value
      echo "$var=$value" >> .env
    }
  done
}

if [ -f .env ]; then
  manage_misc_env
  echo "Miscellaneous configurations set successfully."
else
  echo "Error: .env file not found."
fi
