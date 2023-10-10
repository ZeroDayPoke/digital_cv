#!/usr/bin/env bash

# ./utils/setup_flask.sh
# Manage Flask-related variables in .env
manage_flask_env() {
  flask_vars=("FLASK_DEBUG" "SECRET_KEY" "FLASK_ENV")
  for var in "${flask_vars[@]}"; do
    grep -q "^$var=" .env || {
      read -p "$var: " value
      echo "$var=$value" >>.env
    }
  done
}

manage_flask_env
echo "Flask configurations set successfully."
