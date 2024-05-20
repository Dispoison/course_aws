#!/usr/bin/bash

PROJECT_MAIN_DIR_NAME="course_aws"

sudo cp "/home/ubuntu/$PROJECT_MAIN_DIR_NAME/gunicorn/gunicorn.service" "/etc/systemd/system/gunicorn.service"

sudo systemctl start gunicorn.service
sudo systemctl enable gunicorn.service
