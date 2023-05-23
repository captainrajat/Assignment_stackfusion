from django.db import models
from datetime import datetime


class User(models.Model):
    name = models.CharField(max_length=100, null=False)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
