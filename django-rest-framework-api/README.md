# Setting up Project
django-admin startproject blog
pip install djangorestframework

add rest_framework in settings.py
python manage.py makemigrations
python manage.py migrate

@api_view(['GET']) on method to make a rest api