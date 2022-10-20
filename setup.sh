#!/bin/bash
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata recipes.json
echo "from django.contrib.auth.models import User; User.objects.create_superuser('${DJANGO_SUPERUSER_USERNAME}', '${DJANGO_SUPERUSER_EMAIL}', '${DJANGO_SUPERUSER_PASSWORD}')" | python manage.py shell