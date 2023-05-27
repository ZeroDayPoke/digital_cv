#!/usr/bin/env bash
# sql backup script

rm backup.sql
rm *.tar.gz
mysqldump -uroot -p"$1" --all-databases > backup.sql
tar czf "$(date +"%d-%m-%Y").tar.gz" backup.sql
