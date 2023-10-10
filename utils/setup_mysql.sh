#!/usr/bin/env bash

DB_NAME='digital_cv_dev'
DB_USER='dev_user'
DB_PASSWORD='dev_password'

echo "Creating development database..."

sudo mysql <<EOF
CREATE DATABASE IF NOT EXISTS $DB_NAME;
CREATE USER IF NOT EXISTS '$DB_USER'@'localhost' IDENTIFIED BY '$DB_PASSWORD';
GRANT ALL PRIVILEGES ON $DB_NAME.* TO '$DB_USER'@'localhost';
FLUSH PRIVILEGES;
EOF

echo "Development database created successfully."

# DB_NAME="digital_cv"

# echo "Creating production database..."

# sudo mysql <<EOF
# CREATE DATABASE IF NOT EXISTS $DB_NAME;
# CREATE USER IF NOT EXISTS '$DB_USER'@'localhost' IDENTIFIED BY '$DB_PASSWORD';
# GRANT ALL PRIVILEGES ON $DB_NAME.* TO '$DB_USER'@'localhost';
# FLUSH PRIVILEGES;
# EOF

# echo "Database created successfully."
