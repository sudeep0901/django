from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
# Create your models here.

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class Person(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    dob = models.DateField()
    age = models.IntegerField()
    created_date = models.DateField(auto_now=True)
    url = models.URLField(verbose_name='url', max_length=200, default="")

    class Meta:
        ordering = ["created_date"]