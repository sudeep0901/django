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


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return "%s the place" % self.name


class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "%s the restaurant" % self.place.name


class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "%s the waiter at %s" % (self.name, self.restaurant)
    