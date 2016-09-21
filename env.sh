#!/bin/bash

if [ -z $APP_DIR ]; then
    APP_DIR=/opt
fi

export ANSIBLE_CONFIG="$APP_DIR/ansible.cfg"
export PYTHONPATH="$APP_DIR/ansible/lib"
export PATH="$PATH:/usr/local/bin"

cd $APP_DIR/app

gunicorn ansibleapi.wsgi \
    --bind=0.0.0.0:8000 \
    --timeout 300 \
    --workers 3 \
    --log-level debug \
    --access-logfile /var/log/ansibleapi.log
