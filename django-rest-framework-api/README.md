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



2.1 How to find the query associated with a queryset?

snippet = Snippet.objects.all()
str(snippet.query) 

queryset = Snippet.objects.filter(id__gt=5)       


# Convert database to django models
python manage.py  inspectdb
python manage.py inspectdb > models.py


use db.managed = False in Meta Class to model to use sql views/index


Code chechking with 
--------------------------------------
pip install pycodestyle
pycodestyle {python.py}

pylint {source_file_or_directory}

# pyflakes
--------------------

pyflakes is a verification tool(linter) which checks for Python files for errors. Pyflakes doesn’t verify the style at all but it verifies only logistic errors like the syntax tree of each file individually.

To install it: pip install pyflakes.

Let us take the same example script to test pyflakes

Usage: pyflakes {source_file_or_directory}


# flake8
-----------------------------

Flake8 is just a wrapper around pyflakes, pycodestyle and McCabe script (circular complexity checker) (which is used to detect complex-code).

If we like Pyflakes but also want stylistic checks, we can use flake8, which combines Pyflakes with style checks against PEP 8

To install it: pip install flake8.

Usage: flake8 {source_file_or_directory}

To get statics also flake8 {source_file_or_directory} --statistics


black
----------------------

black is a python code auto-formatter. Black reformats entire files in place and also formats the strings to have double-qoutes.

Black is not configurable(except for line-length).

To install it: pip install black.

Usage: black {source_file_or_directory}

The response we got when we did black test_script.py is
_images/black-formatter.png

Using the file test_script.py as an example


autopep8
---------------------------

autopep8 automatically formats Python code to the PEP8 style. It fixes most of the formatting issues that are reported by pycodestyle.

To install it: pip install autopep8

Usage(to format a file): autopep8 --in-place {file_name}

here --in-place is to make changes to files in place.


yapf
----------------------------------------
Yet another Python formatter is another auto-formatter which is maintained by google. yapf is highly configurable and it has different base configurations, like pep8, Google and Facebook.

To install it: pip install yapf

Usage: yapf -i {source_file_or_directory}

here -i is to make changes to files in place.