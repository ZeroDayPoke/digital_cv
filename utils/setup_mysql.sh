#!/usr/bin/env bash

# ./utils/setup_mysql.sh
# Function to manage database-related variables in .env
manage_db_env() {
  db_vars=("DB_USER" "DB_PASS" "DB_NAME")
  for var in "${db_vars[@]}"; do
    grep -q "^$var=" .env || { read -p "$var: " value; echo "$var=$value" >> .env; }
  done
}

manage_database() {
  local DB=$1
  local USER=$2
  local PASSWORD=$3
  local DROP=$4
  local ACTION=$5

  echo "$ACTION database $DB..."
  
  if [ "$DROP" = "yes" ]; then
    sudo mysql -e "DROP DATABASE IF EXISTS $DB;" || { echo "Failed to drop $DB"; exit 1; }
  fi

  sudo mysql -e "CREATE DATABASE IF NOT EXISTS $DB;" || { echo "Failed to create $DB"; exit 1; }
  sudo mysql -e "CREATE USER IF NOT EXISTS '$USER'@'localhost' IDENTIFIED BY '$PASSWORD';" || { echo "Failed to create user $USER"; exit 1; }
  sudo mysql -e "GRANT ALL PRIVILEGES ON $DB.* TO '$USER'@'localhost';" || { echo "Failed to grant privileges"; exit 1; }
  sudo mysql -e "FLUSH PRIVILEGES;" || { echo "Failed to flush privileges"; exit 1; }
}

# Read .env file if it exists, otherwise prompt for database config
if [ -f .env ]; then
  echo "Reading database configurations from .env file..."
  export $(grep -v '^#' .env | xargs -d '\n')
else
  echo "No .env file found. Please enter the database configurations:"
  read -p "DB User: " DB_USER
  read -p "DB Password: " DB_PASS
  read -p "DB Name: " DB_NAME
  echo "Saving configurations to .env file..."
  echo "DB_USER=$DB_USER" > .env
  echo "DB_PASS=$DB_PASS" >> .env
  echo "DB_NAME=$DB_NAME" >> .env
fi

# Ask to drop existing databases
read -p "Do you want to drop existing databases? (y/N): " DROP_DB
if [ "$DROP_DB" = "y" ] || [ "$DROP_DB" = "Y" ]; then
  DROP="yes"
  ACTION="Recreating"
else
  DROP="no"
  ACTION="Creating"
fi

# Manage databases
manage_database "$DB_NAME" "$DB_USER" "$DB_PASS" "$DROP" "$ACTION"
manage_database "${DB_NAME}_dev" "$DB_USER" "$DB_PASS" "$DROP" "$ACTION"
manage_database "${DB_NAME}_test" "$DB_USER" "$DB_PASS" "$DROP" "$ACTION"

echo "Databases managed successfully."
