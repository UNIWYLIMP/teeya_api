from django.db import models

# Create your models here.


class Contact(models.Model):
    Name = models.CharField(max_length=200, default="")
    Email = models.CharField(max_length=200, default="")
    Telephone = models.CharField(max_length=200, default="")
    QueryDescription = models.CharField(max_length=200, default="")
    Date = models.DateTimeField(auto_now=True)


class Booking(models.Model):
    Name = models.CharField(max_length=200, default="")
    Email = models.CharField(max_length=200, default="")
    Telephone = models.CharField(max_length=200, default="")
    ProjectDescription = models.CharField(max_length=200, default="")
    ProductName = models.CharField(max_length=200, default="")
    Date = models.DateTimeField(auto_now=True)
