from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
     user = models.OneToOneField(User,on_delete=models.CASCADE)
     profile_pic = models.ImageField(upload_to='images',null=True)
     bio = models.CharField(max_length=120)
     birth_date = models.DateField(null=True)

     def __str__(self):
         return str(self.user)