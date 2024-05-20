#!/bin/bash
set -e

GIT_REPO_URL="https://github.com/Dispoison/course_aws.git"

PROJECT_MAIN_DIR_NAME="course_aws"

git clone "$GIT_REPO_URL" "/home/ubuntu/$PROJECT_MAIN_DIR_NAME"

cd "/home/ubuntu/$PROJECT_MAIN_DIR_NAME"

chmod +x scripts/*.sh

./scripts/instance_os_dependencies.sh
./scripts/python_dependencies.sh
./scripts/gunicorn.sh
./scripts/start_app.sh
