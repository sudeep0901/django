from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    dob = models.DateField()
    age = models.IntegerField()
    created_date = models.DateField(auto_now=True)
    url = models.URLField(verbose_name='url', max_length=200, default="")
