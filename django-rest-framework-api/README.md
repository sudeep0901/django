<!-- https://books.agiliq.com -->
# Setting up Project
django-admin startproject blog
pip install djangorestframework

add rest_framework in settings.py
python manage.py makemigrations
python manage.py migrate

@api_view(['GET']) on method to make a rest api

# syntax hilighters
pip install pygments



# DJANGO Extenstions
pip install django-extensions
# pip install jupyter ipython django-extensions
----------------------------------------------------
python manage.py graph_models -a -o myapp_models.png
python manage.py show_urls
python manage.py validate_templates
python manage.py shell_plus

python manage.py runserver_plus

python manage.py shell_plus --notebook
python manage.py shell_plus --print-sql

pip install httpie

# Request and Response DJANGO REST Framework
--------------------------------------------------
request.POST  # Only handles form data.  Only works for 'POST' method.
request.data  # Handles arbitrary data.  Works for 'POST', 'PUT' and 'PATCH' methods.


REST framework provides two wrappers you can use to write API views.

    The @api_view decorator for working with function based views.
    The APIView class for working with class-based views.


http --debug --json POST http://127.0.0.1:8000/snippets/snippets/ code="print(456)"

http --json POST http://127.0.0.1:8000/snippets/snippets/ code="print(456)"

formatting url
http://127.0.0.1:8000/snippets/snippets/1?format=json
http --json GET http://127.0.0.1:8000/snippets/snippets/?format=json




# Hyperlinking our API

Dealing with relationships between entities is one of the more challenging aspects of Web API design. There are a number of different ways that we might choose to represent a relationship:

    Using primary keys.
    Using hyperlinking between entities.
    Using a unique identifying slug field on the related entity.
    Using the default string representation of the related entity.
    Nesting the related entity inside the parent representation.
    Some other custom representation.
