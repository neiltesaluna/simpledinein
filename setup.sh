#!/bin/bash
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata recipes.json
python manage.py createsuperuser --noinput
gunicorn simpledinein.wsgi --bind 0.0.0.0:8000 --workers=$(nproc)