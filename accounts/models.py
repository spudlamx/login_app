from django.db import models

# Create your models here.
class Accounts(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)