from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Person(models.Model):
    Aadhar_id = models.IntegerField()
    email = models.CharField(max_length=1000)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone_no = models.IntegerField()


class Items_listed(models.Model):
    lender_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    Item_id = models.IntegerField()
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()
    location = models.CharField(max_length=1000)
    status = models.CharField(max_length=10)


class borrower(models.Model):
    Item_id = models.ForeignKey(Items_listed, on_delete=models.CASCADE)
    borrow_id = models.IntegerField()
    amount = models.IntegerField()
    borrow_date = models.DateField()
    return_date = models.DateField()
