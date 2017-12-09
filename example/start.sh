#!/bin/bash

python3 /code/manage.py makemigrations
python3 /code/manage.py migrate admin
python3 /code/manage.py migrate polls
python3 /code/manage.py migrate colorfield
python3 /code/manage.py migrate
python3 /code/manage.py collectstatic --noinput
python3 /code/manage.py runserver 0.0.0.0:8000
