#!/bin/bash

if [[ $# -ne 2 ]]; then
    echo "Usage: install.sh <admin-password> <host>"
    exit 1
fi

cd /var/www/html

echo "Installing Nextcloud ..."
php occ maintenance:install --admin-pass="$1" --no-interaction
php occ config:system:set trusted_domains 1 --value="$2"

echo "Installing app mail ..."
php occ app:install mail

echo "Installing app user_external ..."
php occ app:install user_external

echo "Installing app external ..."
php occ app:install external

echo "Installing app onlyoffice ..."
php occ app:install documentserver_community
php occ app:install onlyoffice

echo "Importing settings ..."
php occ config:import < /install/config.json

echo "Setup complete"

echo "Now go to https://$2"
echo "User: admin"
echo "Password: $1"

