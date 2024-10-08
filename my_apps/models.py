from django.db import models

# Create your models here.
class application(models.Model):
    First_Name=models.CharField(max_length=30)
    Last_Name=models.CharField(max_length=30)
    password=models.IntegerField()
    Address=models.CharField(max_length=100)
