#!/usr/bin/env bash

# ./utils/setup_admin.sh
# Manage admin-related variables in .env

manage_admin_env() {
  admin_vars=("DEFAULT_ADMIN_EMAIL" "DEFAULT_ADMIN_PASSWORD" "DEFAULT_ADMIN_USERNAME")
  for var in "${admin_vars[@]}"; do
    if ! grep -q "^$var=" .env; then
      read -p "$var: " value

      if [ "$var" == "DEFAULT_ADMIN_EMAIL" ]; then
        validate_email "$value"
      elif [ "$var" == "DEFAULT_ADMIN_PASSWORD" ]; then
        validate_password "$value"
      fi

      echo "$var=$value" >> .env
    fi
  done
}

if [ -f .env ]; then
  manage_admin_env
  echo "Admin credentials set successfully."
else
  echo "Error: .env file not found."
fi
