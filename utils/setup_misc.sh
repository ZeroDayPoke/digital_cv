# ./utils/setup_misc.sh

# Function to manage miscellaneous variables in .env
manage_misc_env() {
    misc_vars=("DB_HOST" "FLASK_APP_HOST" "FLASK_APP_PORT" "EMAIL_SERVICE_URL")
    for var in "${misc_vars[@]}"; do
        grep -q "^$var=" .env || {
            read -p "$var: " value
            echo "$var=$value" >>.env
        }
    done
}

manage_misc_env
echo "Miscellaneous configurations set successfully."
