FROM docker.io/matrixdotorg/synapse:latest

COPY ./getSitePackagePath.py .
RUN python getSitePackagePath.py

COPY ./auth_provider/imap_auth_provider.py ${SITE_PACKAGES}/imap_auth_provider.py