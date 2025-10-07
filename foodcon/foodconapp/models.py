# models.py
from django.db import models

class UserRegistration(models.Model):
     first_name = models.CharField(max_length=50)
     last_name = models.CharField(max_length=50)
     place = models.CharField(max_length=100)
     phone = models.CharField(max_length=10)
     email = models.EmailField(unique=True)
     username = models.CharField(max_length=50, unique=True)
     password = models.CharField(max_length=255)

     def __str__(self):
       return self.username
    
##class chefRegistration(models.Model):
    ##first_name = models.CharField(max_length=50)
   ## last_name = models.CharField(max_length=50)
    ##place = models.CharField(max_length=100)
   ## phone = models.CharField(max_length=10)
   ## email = models.EmailField(unique=True)
    ##username = models.CharField(max_length=50, unique=True)
    ##password = models.CharField(max_length=255)

    ##def __str__(self):
      ##  return self.username

