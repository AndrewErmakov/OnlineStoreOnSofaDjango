#!/bin/bash

python manage.py makemigrations
python manage.py migrate --no-input
python manage.py collectstatic --no-input


gunicorn online_store_on_sofa_project.wsgi:application --bind 0.0.0.0:8000