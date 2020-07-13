Installation
============

### Requirements

Minimum requirements are 2GB RAM and 2GB memory, however to get the best experience use a machine with > 4GB RAM. 
Since this project is built on docker-compose, please also make sure you have `docker` (version > 19.03) and `docker-compose` (version > 1.25) installed.

We recommend getting the project sources by cloning them from this repository. Therefore you also need to have `git` installed.


The latest source code was tested with this docker configuration.
```
$ docker version
Client: Docker Engine - Community
 Version:           19.03.8
 API version:       1.40
 Go version:        go1.12.17
 Git commit:        afacb8b7f0
 Built:             Wed Mar 11 01:26:02 2020
 OS/Arch:           linux/amd64
 Experimental:      false

Server: Docker Engine - Community
 Engine:
  Version:          19.03.8
  API version:      1.40 (minimum version 1.12)
  Go version:       go1.12.17
  Git commit:       afacb8b7f0
  Built:            Wed Mar 11 01:24:36 2020
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.2.13
  GitCommit:        7ad184331fa3e55e52b890ea95e65ba581ae3429
 runc:
  Version:          1.0.0-rc10
  GitCommit:        dc9208a3303feef5b3839f4323d9beb36df0a9dd
 docker-init:
  Version:          0.18.0
  GitCommit:        fec3683
$docker-compose version
docker-compose version 1.25.4, build 8d51620a
docker-py version: 4.1.0
CPython version: 3.7.5
OpenSSL version: OpenSSL 1.1.0l  10 Sep 2019
```

#### Make sure your server is reachable
Make sure you set the A records in your domain management software to point to the ip-address of the docker host. 

Also don't forget to assign the subdomains for nextcloud, mail, riot, and synapse to this ip address. This can either be done by assigning the individual subdomains to the docker host or placing a wildcard dns entry (\*.yourdomain.com)

In order to **receive E-Mails**, don't forget to set the MX and SPF records. An in-depth article can be found in the [Mailu Documentation](https://mailu.io/master/dns.html).



### Get the source

#### 1. Create a new directory where all the docker files and config will live:

```bash
mkdir /etc/dockercloud
```

#### 2. Clone this repository 

```bash
git clone https://github.com/author/cloud -C /etc/dockercloud
cd /etc/dockercloud
```

#### 3. Set the basic configuration

In order the get Project Docker Cloud online, you need to change basic settings in three environment files:

```env
# .env
DOMAIN

# nextcloud.env
MYSQL_ROOT_PASSWORD
MYSQL_PASSWORD

# synapse.env
POSTGRES_PASSWORD
```

A full reference to all configurable parameters is given in [CONFIGURATION.md](CONFIGURATION.md)

#### 4. Create synapse keys and folder structure

```bash
./synapse/setup.sh
```

This will run the `generate` command inside the *synapse* container.


#### 5. Download and start the containers

```bash
docker-compose up -d
```

#### 6. Finish the nextcloud installation
You have to pass the host of your nextcloud installation to the install script, for the default, this 
is `cloud.<your.domain.com>`.


```bash
docker-compose exec --user www-data nextcloud /install/install.sh <nextcloud-admin-password> <host>
```
