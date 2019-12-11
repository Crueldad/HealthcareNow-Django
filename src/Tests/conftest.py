import os
import django
from django.conf import settings
import pytest


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HealthCareNow.settings')

def pytest_configure():
    settings.DEBUG = False
    django.setup()