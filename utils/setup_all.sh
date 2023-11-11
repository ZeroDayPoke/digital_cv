#!/usr/bin/env bash

# ./utils/setup_all.sh

if [ ! -f .env ]; then
  touch .env
fi

bash ./utils/setup_admin.sh
bash ./utils/setup_flask.sh
bash ./utils/setup_misc.sh
bash ./utils/setup_image.sh
bash ./utils/setup_mysql.sh

echo "Complete setup finished."
