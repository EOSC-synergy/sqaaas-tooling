#!/bin/bash
set -e
python /opt/setup-rucio-jupyterlab/configure.py

# Creation of the rucio.cfg file
mkdir -p /certs /tmp;
echo -n $RUCIO_ACCESS_TOKEN > /tmp/rucio_oauth.token;

exec "$@"
