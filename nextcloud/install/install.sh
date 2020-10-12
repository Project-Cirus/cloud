#!/bin/bash


cd /var/www/html

echo "Installing app mail ..."
php occ app:install mail

echo "Installing app user_external ..."
php occ app:install user_external

echo "Installing app external ..."
php occ app:install external

echo "Installing collabora ..."
php occ app:install richdocuments
php occ app:install richdocumentscode

echo "Installing app fulltextsearch ..."
php occ app:install files_fulltextsearch
php occ app:install files_fulltextsearch_tesseract
php occ app:install fulltextsearch
php occ app:install fulltextsearch_elasticsearch

echo "Installing app riotchat ..."
php occ app:install riotchat

echo "Importing settings ..."
php occ config:import < /install/config.json

echo "Copying skeleton files ..."
cp /install/Mail_Setup.png core/skeleton/Mail_Setup.png

echo "Creating initial search index ..."
php occ fulltextsearch:index

echo "Setup complete"

echo "Now go to https://$NEXTCLOUD_TRUSTED_DOMAINS"
echo "User: $NEXTCLOUD_ADMIN_USER"
echo "Password: $NEXTCLOUD_ADMIN_PASSWORD"

