from django.db import models
from django.contrib.auth.models import User



class Student(models.Model):
    gengerChoice = [('male', 'Male'), ('female', 'Female')]

    name = models.CharField(max_length = 255)
    email = models.EmailField(max_length=255)
    age = models.IntegerField()
    gender =models.CharField(choices= gengerChoice, max_length = 10)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
