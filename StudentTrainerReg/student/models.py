from django.db import models

# Create your models here.


class StudRegister(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class StudComplete(models.Model):
    username = models.CharField(max_length=100,unique=True)
    phonenumber = models.IntegerField()
    address = models.CharField(max_length=100)
    education = models.CharField(max_length=50)
    details = models.CharField(max_length=150)
    year = models.FloatField()
    percentage = models.IntegerField()
    course = models.CharField(max_length=100)
    mode = models.CharField(max_length=100)



