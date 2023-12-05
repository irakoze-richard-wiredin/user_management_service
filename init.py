# create_superuser.py
import os
import django
from decouple import config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_management_service.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(config('SUPERUSER_USERNAME'), config('SUPERUSER_PASSWORD'), config('SUPERUSER_EMAIL'))
