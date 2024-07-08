#!/bin/sh
cp /root/server/.env.docker /root/.env # extra
set -a  # Read all environment variables from the file
. /root/server/.env.docker
export MT_FILES_DIR  # Export the desired variable
#
fastapi run /root/server/main.py