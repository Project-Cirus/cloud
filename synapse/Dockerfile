FROM docker.io/matrixdotorg/synapse:v1.20.1

COPY ./getSitePackagePath.py .
RUN python getSitePackagePath.py

COPY ./auth_provider/imap_auth_provider.py /usr/local/lib/python3.7/site-packages/imap_auth_provider.py
