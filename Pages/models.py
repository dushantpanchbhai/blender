from django.db import models

# Create your models here.

class Account(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)

class Models(models.Model):
    img=models.ImageField(upload_to='images',blank=True,null=True)
    link=models.URLField(max_length=50)
    title=models.CharField(max_length=200)

class Tutorial(models.Model):
    title=models.CharField(max_length=100)
    url=models.URLField(max_length=250)
    
