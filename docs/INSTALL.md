Installation
============

### Requirements

Minimum requirements are 2 cpu cores and 4GB memory, however to get the best experience use a machine with more RAM. 
Since this project is built on docker-compose, please also make sure you have `docker` (version > 19.03) and `docker-compose` (version > 1.25) installed.

We recommend getting the project sources by cloning them from this repository. Therefore you also need to have `git` installed.


The latest source code was tested with this docker configuration.
```
$ docker version
Client: Docker Engine - Community
 Version:           19.03.13
 API version:       1.40
 Go version:        go1.13.15
 Git commit:        4484c46d9d
 Built:             Wed Sep 16 17:02:36 2020
 OS/Arch:           linux/amd64
 Experimental:      false

Server: Docker Engine - Community
 Engine:
  Version:          19.03.13
  API version:      1.40 (minimum version 1.12)
  Go version:       go1.13.15
  Git commit:       4484c46d9d
  Built:            Wed Sep 16 17:01:06 2020
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.3.7
  GitCommit:        8fba4e9a7d01810a393d5d25a3621dc101981175
 runc:
  Version:          1.0.0-rc10
  GitCommit:        dc9208a3303feef5b3839f4323d9beb36df0a9dd
 docker-init:
  Version:          0.18.0
  GitCommit:        fec3683
```
```
$ docker-compose version
docker-compose version 1.27.4, build 40524192
docker-py version: 4.3.1
CPython version: 3.7.7
OpenSSL version: OpenSSL 1.1.0l  10 Sep 2019
```

#### Make sure your server is reachable
Make sure you set the A records in your domain management software to point to the ip-address of the docker host. 

Also don't forget to assign the subdomains for nextcloud, mail, riot, and synapse to this ip address. This can either be done by assigning the individual subdomains to the docker host or placing a wildcard dns entry (\*.example.com)

In order to **receive E-Mails**, don't forget to set the MX and SPF records. An in-depth article can be found in the [Mailu Documentation](https://mailu.io/master/dns.html).

Example Subdomain Settings:

```
*.example.com - A - YOUR-SERVER-IP
or
cloud.example.com - A - YOUR-SERVER-IP
synapse.example.com - A - YOUR-SERVER-IP
riot.example.com - A - YOUR-SERVER-IP
mail.example.com - A - YOUR-SERVER-IP
```
Example Mail Settings:
```
MX 10 - mail.example.com.
TXT - v=spf1 mx a:mail.example.com -all
```


### Get the source
On your host server create a new project directory and make sure your user has read, write and execute rights to the directory.</p>
It might be a good idea to create a new user for this project. It is important that this user is allowed to run ```docker``` and ```docker-compose``` commands. For this purpose you might want to add your user to the ```sudo``` group.

```
  $ mkdir /srv/projectcirus
  $ cd /srv/projectcirus
  $ wget -O projectcirus.tar.gz {{zipPath}}
  $ tar -xzf projectcirus.tar.gz --strip 1
```
Please review your downloaded and extracted files.

### Create synapse keys and folder structure
This will run the ```generate```-command to generate keys for the synapse container.

```
$ ./synapse/setup.sh
```

### Download and start the containers

```
$ sudo docker-compose up -d
```

### Install additional nextcloud apps and finish configuration

```
$ sudo docker-compose exec --user www-data nextcloud /install/install.sh
```

### Create the initial index for full text search

```
$ sudo docker exec -u www-data projectcirus_nextcloud_1 php occ fulltextsearch:index
```

### Create a cron job for your nextcloud on your host system (example for Ubuntu)

```
$ sudo crontab -e
```

Add the following to your crontab:

```
*/5 * * * * /usr/bin/docker exec --user www-data projectcirus_nextcloud_1 php -f cron.php > /dev/null 2>&1
```

### Congratulations on setting up your cloud!

You can now log into your mail server to create new users, log into nextcloud to collaboratively work on documents, use the chat client and much more!
