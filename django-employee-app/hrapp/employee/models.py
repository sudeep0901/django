from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Employer(models.Model):
    class Meta:
        db_table ="employer"
    name = models.CharField(max_length=255, unique=True)
    address = models.TextField(verbose_name="address_of_employer", default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)


class Employee(models.Model):
    class Meta:
        db_table = "employee"
    user = models.ForeignKey(User, on_delete= models.CASCADE, null=False)
    name = models.CharField(max_length=255,null=False)
    email = models.EmailField(max_length=254, null=False)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)








