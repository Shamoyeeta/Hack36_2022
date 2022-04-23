from django.db import models


# Create your models here.
class Person(models.Model):
    Aadhar_id = models.IntegerField()
    email = models.EmailField(max_length=1000, default="test@test.com")
    password = models.CharField(max_length=50, default="password")
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
    type = models.CharField(max_length=50, default="No Category")
    status = models.CharField(max_length=10)


class borrower(models.Model):
    Item_id = models.ForeignKey(Items_listed, on_delete=models.CASCADE)
    borrow_id = models.IntegerField()
    amount = models.IntegerField()
    borrow_date = models.DateField()
    return_date = models.DateField()
