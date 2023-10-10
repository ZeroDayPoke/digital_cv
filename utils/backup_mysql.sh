#!/usr/bin/env bash

# ./utils/backup_mysql.sh
# SQL backup script
# Check if argument provided
if [ -z "$1" ]; then
  echo "Missing password argument."
  exit 1
fi

# Remove previous backups
rm -f backup.sql
rm -f *.tar.gz

# Perform backup
sudo mysqldump -uroot -p"$1" --all-databases > backup.sql
tar czf "$(date +"%Y-%m-%d").tar.gz" backup.sql
echo "Backup completed successfully."
