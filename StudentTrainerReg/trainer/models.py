from django.db import models

# Create your models here.


class TrainerRegister(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class TrainerComplete(models.Model):
    username = models.CharField(max_length=100)
    phonenumber = models.IntegerField()
    address = models.CharField(max_length=100)
    education = models.CharField(max_length=50)
    details = models.CharField(max_length=150)
    year = models.FloatField()
    percentage = models.IntegerField()
    expert = models.CharField(max_length=100)
    experience = models.FloatField(null=True)
    available = models.CharField(max_length=100)
    hours=models.FloatField(null=True)
    mode=models.CharField(max_length=100)
    days=models.CharField(max_length=100)
