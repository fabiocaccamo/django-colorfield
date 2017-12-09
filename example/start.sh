#!/bin/bash

python3 /code/manage.py makemigrations admin
python3 /code/manage.py makemigrations polls
python3 /code/manage.py migrate
python3 /code/manage.py collectstatic --noinput
python3 /code/manage.py runserver 0.0.0.0:8000
