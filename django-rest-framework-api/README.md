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




DJANGO
------------------------------------
Once a model has been processed by Python, along with Django’s ModelBase metaclass, its original structure can still
be determined by using an attribute that exists on every Django model and its instances called _meta.
# meta_ instance exists with every django model
# add_to_class - use to add attribute to any existing django model object
File.add_to_class("expiration_date", models.DateField(null=True, blank=True))
File.add_to_class("method_x", method_x)

# Django Jupyter Notebook Extenstion code to run in notebook
-------------------------------------------------------------
```python
import os, sys
PWD = os.getenv('PWD')
os.chdir(PWD)
sys.path.insert(0, os.getenv('PWD'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "local_settings.py")
import django
django.setup()

# django Models
-----------------------------------------
from django.utils.text import capfirst   

# list of fields
snippet._meta.fields


for field in Snippet._meta.fields: 
    name = capfirst(field.verbose_name) 
    value = getattr(Snippet, field.name) 
    print("field name %s, value %s" % (name, value)) 


for field in Snippet._meta.fields: 
    name = capfirst(field.verbose_name) 
    value = getattr(Snippet, field.name) 
    print("field name %s, value %s" % (name, field.__class__)) 



Snippet._meta.get_field('code').__class__     

# Primary Key Fields
Snippet._meta.pk
Snippet._meta.has_auto_field - depreceted
Snippet._meta.auto_field

# Model Configuration with Meta Class in Model are stored in _meta 
Snippet._meta.ordering
Snippet._meta.app_label 


abstract—A Boolean that indicates whether the model was defined as abstract, a process that
is described in more detail in Django’s model inheritance documentation. 2 The default value
is False.
• app_label—A string containing the name Django uses to recognize the application where the
model was defined. It’s easiest to understand what this means by looking at the default value,
which is the name of the module containing the models.py the model is specified in. For a
model located at corporate.accounts.models.Account, the app_label would be "accounts".
• db_table—The name of the database table that Django will use to store and retrieve data for
the model. If not defined explicitly, it’s determined as a function of the model’s name and
location. That is, the db_table for a model called Account with an app_label of accounts
would be "accounts_account".
• db_tablespace—In the case of Oracle, and perhaps other database backends in the future,
tables can be placed in different parts of the disk, or different disks entirely. By default, this is
simply an empty string, which tells the database to store the table in its default location. This
option is ignored for backends that don’t support it.
• get_latest_by—The name of a date-based field, such as a DateField or a DateTimeField,
which should be used to determine the most recent instance of a model. If not provided, this
will be an empty string.

order_with_respect_to—An instance of a field relating to another model, which is used
when ordering instances of this model. This defaults to None, which implies that the model’s
ordering is determined solely by fields within the model itself, rather than any related models.
• ordering—A tuple containing the names of fields to be used when ordering instances of
the model. By default, this is an empty tuple, which relies on the database to determine the
ordering of model instances.
• permissions—A sequence of tuples of additional permissions to be added to the model. Each
tuple in the sequence contains two values, the first being the name of the permission to be
used in code and in the database, and the second being the text to be displayed in the admin
interface when selecting permissions for a user or group.
• unique_together—A sequence of tuples indicating any groups of fields that must, when
combined, be used in only one record in the database. Each tuple in the sequence contains the
names of the fields that must be unique together for a particular index. Multiple tuples don’t
have any relation to each other; they each represent a separate index at the database level.
• verbose_name—The display name for a single instance of the model. By default, this is
determined by the name of the class itself, by splitting up each capitalized portion into a
separate uncapitalized word; Article would become "article", while AddressBook would
become "address book".

verbose_name_plural—The display name for multiple instances of the model. By default, this
will be simply the verbose_name with an “s” at the end. Article would be "articles" and
AddressBook would be "address books".
• verbose_name_raw—The raw, untranslated version of verbose_name. Occasionally, it’s
necessary to use the same display name for everyone, without Django applying a translation.
This is particularly useful when storing it away in the cache or database for later access,
especially if it’ll be translated at a later point in time.


# Accessing the Model Cache
Once models have been processed by the ModelBase metaclass, they’re placed in a global registry called AppCache, located at django.db.models.loading. This is instantiated automatically, immediately when the module is imported, and is accessed using the name cache. This special cache provides access to the various models that are known to Django, as well as installs new ones if necessary.



# django.db.models.loading.get_model() has been removed in django 1.9.

You are supposed to use django.apps instead.

 ```python  
   from django.apps import apps
   apps.get_models()  is replacement of get_cache()
   apps.get_model('snippets', 'snippet')          



#### contribute_to_class(self, cls, name)
* Instead, by using a metaclass, Django can intercede at the point where Python is processing the class, and use the presence of a contribute_to_class() method to identify objects that need to be handled differently. If this method exists, it’s called instead of the standard setattr(), allowing the field to register itself in whatever way is most appropriate for its purpose. When doing so, Django also provides the class itself as an argument, as well as the name it was given, which was discovered while looking through the attributes assigned to the class. Therefore, in addition to the usual self, this method receives two arguments.



### CONTRIBUTE_TO_CLASS() VS SETATTR()
There is one very important thing to keep in mind when dealing with contribute_to_class() . It’s been
mentioned a few times already in various places, but it’s so important that it merits driving home very explicitly.
If Django identifies an object as having a contribute_to_class() method, only that method will be called.
Normally, setattr() is used to set attributes on an object such as a class, but since model fields don’t get set in
the standard namespace, that step is skipped intentionally. Therefore, if a custom field does in fact need to be set
as an attribute on the model class itself, doing so is the sole responsibility of the field itself, during the execution
of its contribute_to_class() method.
Sometimes, fields will instead need to set some other object, such as a descriptor, as the attribute on the class,
to provide additional customizations for other types of access. This, too, is the responsibility of the field class, and
the only time to do so in a way that will maintain the appearance of a standard field is during the execution of its
contribute_to_class() method.




* There is one very important thing to keep in mind when dealing with contribute_to_class() . It’s been mentioned a few times already in various places, but it’s so important that it merits driving home very explicitly. If Django identifies an object as having a contribute_to_class() method, only that method will be called. Normally, setattr() is used to set attributes on an object such as a class, but since model fields don’t get set in the standard namespace, that step is skipped intentionally. Therefore, if a custom field does in fact need to be set
as an attribute on the model class itself, doing so is the sole responsibility of the field itself, during the execution of its contribute_to_class() method.

