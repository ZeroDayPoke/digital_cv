#!/usr/bin/env bash

# ./utils/setup_misc.sh

manage_misc_env() {
  misc_vars=("EMAIL_SERVICE_URL", "EMAIL_USERNAME", "EMAIL_PASSWORD")
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
