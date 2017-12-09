#!/bin/bash

python3 manage.py makemigrations admin
python3 manage.py makemigrations polls
python3 manage.py migrate
python3 manage.py collectstatic --noinput
python3 manage.py runserver 0.0.0.0:8000
