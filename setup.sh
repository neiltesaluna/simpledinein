#!/bin/bash
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata recipes.json
python manage.py --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL --password $DJANGO_SUPERUSER_PASSWORD