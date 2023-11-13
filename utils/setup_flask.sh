#!/usr/bin/env bash

# ./utils/setup_flask.sh
# Manage Flask-related variables in .env

generate_secret_key() {
  python -c "import os; print(os.urandom(24).hex())"
}

manage_flask_env() {
  flask_vars=("FLASK_DEBUG" "SECRET_KEY" "FLASK_APP_ENV" "FLASK_APP_DOMAIN" "FLASK_APP_PORT")
  for var in "${flask_vars[@]}"; do
    if ! grep -q "^$var=" .env; then
      if [ "$var" == "SECRET_KEY" ]; then
        echo "SECRET_KEY=$(generate_secret_key)" >> .env
      else
        read -p "$var: " value
        echo "$var=$value" >> .env
      fi
    fi
  done
}

if [ -f .env ]; then
  manage_flask_env
  echo "Flask configurations set successfully."
else
  echo "Error: .env file not found."
fi
