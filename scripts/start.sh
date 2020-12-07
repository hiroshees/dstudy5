#!/bin/bash

# kill gunicorn if exist
pkill gunicorn

set -e
HOME=/home/ec2-user/workspace_python
ENV=$HOME/venv_app/bin/activate
PROJECT_PATH=$HOME/dstudy5
SETTINGS_PATH=$PROJECT_PATH/config/settings
GUNICORN=gunicorn
GUNICORN_CONF=$SETTINGS_PATH/gunicorn.py
LOG_DIR=$PROJECT_PATH/logs/gunicorn

mkdir -p $LOG_DIR
touch $LOG_DIR/access.log
touch $LOG_DIR/error.log

cd $SETTINGS_PATH
source $ENV
export PYTHONPATH=$PROJECT_PATH
exec $GUNICORN config.wsgi \
        --access-logfile $LOG_DIR/access.log \
        --error-logfile  $LOG_DIR/error.log \
        --capture-output \
	-c $GUNICORN_CONF \
	-D

