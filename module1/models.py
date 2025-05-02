from django.db import models

# Create your models here.
class Demo(models.Model):
    """name : str
    price : int
    yn : bool"""
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    yn=models.BooleanField(default=False)
class Record(models.Model):
    username=models.CharField(max_length=100)
    date=models.DateField()
    text=models.TextField()
class Samp(models.Model):
    text1=models.CharField(max_length=50)
    text2=models.CharField(max_length=50)