#!/bin/bash
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata recipes.json
python manage.py createsuperuser --noinput