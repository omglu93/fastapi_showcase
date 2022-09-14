#! /usr/bin/env bash

#Start docker container
docker-compose up --force-recreate -d

# Let the DB start
python pre_start.py

# Run migrations
alembic upgrade head

# Run API
python main.py