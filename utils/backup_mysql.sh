#!/usr/bin/env bash

# ./utils/backup_mysql.sh
# SQL backup script

if [ -z "$1" ]; then
  echo "Missing password argument."
  exit 1
fi

backup_file="backup_$(date +"%Y-%m-%d_%H-%M-%S").sql"
backup_archive="backup_$(date +"%Y-%m-%d_%H-%M-%S").tar.gz"

sudo mysqldump -uroot -p"$1" --all-databases > "$backup_file"
tar czf "$backup_archive" "$backup_file"
echo "Backup completed successfully: $backup_archive"
