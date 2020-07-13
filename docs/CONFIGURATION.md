Configuration
=============

The main settings for the project can be altered in different project files. 

## Nextcloud 

Configuration parameters for Nextcloud can be found in [nextcloud.env](nextcloud.env). The following list is non-exhaustive. All environment variables to be configured can be found in the [Nextcloud Documentation](https://github.com/nextcloud/docker#auto-configuration-via-environment-variables)

- `NEXTCLOUD_ADMIN_USER` Name of the Nextcloud admin user.
- `NEXTCLOUD_ADMIN_PASSWORD` Password for the Nextcloud admin user.

- `MYSQL_DATABASE` Name of the database using mysql / mariadb.
- `MYSQL_USER` Username for the database using mysql / mariadb.
- `MYSQL_PASSWORD` Password for the database user using mysql / mariadb.
- `MYSQL_HOST` Hostname of the database server using mysql / mariadb.

## Mailu

Configuration parameters for Mailu can be found in [mailu.env](mailu.env). The following list is non-exhaustive. All environment variables for configuring Mailu can be found in the [Mailu configuration reference](https://mailu.io/master/configuration.html)

- `INITIAL_ADMIN_ACCOUNT` Is used to define the first part of the initial admin address. For simplicity this should be the same as the POSTMASTER address. (Default: admin)
- `INITIAL_ADMIN_DOMAIN` The domain appendix. Most probably identical to the DOMAIN variable.
- `INITIAL_ADMIN_PW` The chosen initial password for the admin user. (Default: password)
- `SECRET_KEY` Set to a randomly generated 16 bytes string
- `SUBNET` Subnet of the docker network. This should not conflict with any networks to which your system is connected. 
- `HOSTNAMES`  Hostnames for this server, separated with comas (Default value: mail.${DOMAIN}) When this is updated, do not forget to update the `VIRTUAL_HOST` and `LETSENCRYPT_HOST` for the service `front` in `docker-compose.yml`
- `POSTMASTER` Postmaster local part (will append the main mail domain). This address is used as the sender address when notifications are issued.
- `DISABLE_STATISTICS` Opt-out of statistics, replace with "True" to opt out
- `ANTIVIRUS` Is currently set to `clamav` ([ClamAV](https://www.clamav.net/)). Can be disabled if hosted on low-memory hosts. Deactivating ClamAV allows the host to consume 512M to 1G less RAM.
- `MESSAGE_SIZE_LIMIT` Message size limit in bytes (Defualt: 50M)
- `WELCOME` Welcome email, enable and set a topic (`WELCOME_SUBJECT`) and body (`WELCOME_BODY`) if you wish to send welcome emails to all users.


## Synapse

Configuration for synapse is stored in the yaml format in [synapse/config/homeserver.yml](synapse/config/homeserver.yml). All configuration parameters are stored in this file and are documented inline.

## Riot

Configuration for the Riot client is stored in the json format in [riot/config.json](riot/config.json). A complete list of configuration items can be found on the Riot [configuration documentation](https://github.com/vector-im/riot-web/blob/develop/docs/config.md). 

- `default_server_config` This sets the default homeserver and identity server URL for Riot to use. The object is the same as returned by https://<server_name>/.well-known/matrix/client, with added support for a `server_name` under the `m.homeserver` section to display a custom homeserver name. Alternatively, the config can contain a `default_server_name` instead which is where Riot will go to get that same object, although this option is deprecated - see the .well-known link above for more information on using this option. Note that the default_server_name is used to get a complete server configuration whereas the `server_name` in the `default_server_config` is for display purposes only.
