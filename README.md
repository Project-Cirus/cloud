☁️ Project Cirus
=============

Project Cirus creates a seamless group collaboration solution by combining industry leading cloud tools. Includes file-sharing, online-document-editing, e-mail, instant messanging, and more. Easy to deploy, maintain and extend. 

## Included Packages

- *[Nextcloud](https://nextcloud.com)* offers an on-premise Universal File Access and sync platform with powerful collaboration capabilities and desktop, mobile and web interfaces.
- *[ONLYOFFICE](https://onlyoffice.com)* is an online office suite comprising viewers and editors for texts, spreadsheets and presentations, fully compatible with Office Open XML formats: .docx, .xlsx, .pptx and enabling collaborative editing in real time.
- *[Mailu](https://mailu.io)* is a simple yet full-featured mail server as a set of Docker images.
- *[Riot.im](https://about.riot.im/)* is a chat app, based on the Matrix protocol. State of the art end-to-end encryption ensures that private communication stays private.

## Installation
A detailed installation procedure is given in [INSTALL.md](docs/INSTALL.md).
We have provided a [setup tool](https://project-cirus.github.io/index.html) which allows you to easily fill in neccesary parameters and guides you through the setup and installaiton process.

Information on authentication and user settings is documented in [SETUP.md](docs/SETUP.md).

We decided to host nextcloud by default under the subdomain *cloud* to allow the main domain to be free to serve your website. How to host a website in this context is explained in [HOWTO Website](HOWTO_WEBSITE.md). 

### Requirements

Minimum requirements are 2GB RAM and 2GB memory, however to get the best experience use a machine with > 4GB RAM. 
Since this project is built on docker-compose, please also make sure you have `docker` (version > 19.03) and `docker-compose` (version > 1.25) installed.

We recommend getting the project sources by cloning them from this repository. Therefore you also need to have `git` installed.



## Contribute

Project Cloud is an open-source project licensed under the MIT license. Feel free to post any suggestions that you may have or want to include by submitting an issue in the repo. 
To make it better, submit pull requests to help fix errors, improve the installation procedure or add new features.

Please follow the [Contibuting Guidelines](CONTRIBUTING.md).

