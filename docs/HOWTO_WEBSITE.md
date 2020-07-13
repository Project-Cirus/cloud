HOWTO Website
=============

Many organizations have their own hosted website, running on the same or a different host.

## Same host

Simply add add your web containers to the [docker-compose.yml](../docker-compose.yml). To make them accessible from the nginx-proxy, add the following envionment variables to the container delivering your website:

```yml
environment:
  - VIRTUAL_HOST=your.domain.com
  - LETSENCRYPT_HOST=your.domain.com
  - LETSENCRYPT_EMAIL=admin@your.domain.com
```

Don't expose port 80 on the web container, nginx-proxy will choose it automatically for you. If your container uses a different port for listening to http-traffic, also assign the environment variable `VIRTUAL_PORT`.
Don't use SSL to encrypt your traffic, since the nginx-proxy will handle encyption.

### Example: Wordpress

```yml
wpdb:
 image: mysql:5.7
 volumes:
   - db_data:/var/lib/mysql
 restart: always
 environment:
   - MYSQL_ROOT_PASSWORD: somewordpress
   - MYSQL_DATABASE: wordpress
   - MYSQL_USER: wordpress
   - MYSQL_PASSWORD: wordpress

wordpress:
 depends_on:
   - wpdb
 image: wordpress:latest
 restart: always
 environment:
   - WORDPRESS_DB_HOST: wpdb:3306
   - WORDPRESS_DB_USER: wordpress
   - WORDPRESS_DB_PASSWORD: wordpress
   - WORDPRESS_DB_NAME: wordpress
   - VIRTUAL_HOST=your.domain.com
   - LETSENCRYPT_HOST=your.domain.com
   - LETSENCRYPT_EMAIL=admin@your.domain.com
```

## Different host
If you want to host your website on a differnt host than where dockercloud is hosted, simply only point the DNS-records for nextcloud, mailu, synapse and riot to host running them. 
