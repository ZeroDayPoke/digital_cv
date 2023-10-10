#!/usr/bin/env bash

# ./utils/setup_admin.sh
# Manage admin-related variables in .env
manage_admin_env() {
  admin_vars=("DEFAULT_ADMIN_EMAIL" "DEFAULT_ADMIN_PASSWORD" "DEFAULT_ADMIN_USERNAME")
  for var in "${admin_vars[@]}"; do
    grep -q "^$var=" .env || { read -p "$var: " value; echo "$var=$value" >> .env; }
  done
}

manage_admin_env
echo "Admin credentials set successfully."
