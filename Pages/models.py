from django.db import models
import datetime
# Create your models here.

class Account(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Models(models.Model):
    img = models.ImageField(upload_to='images',blank=True,null=True)
    title=models.CharField(max_length = 100)
    link=models.CharField(max_length=200,blank=True,null=True)
    downloads = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Tutorial(models.Model):
    # index=models.IntegerField(blank=True, null=True)
    title=models.CharField(max_length=100)
    url=models.URLField(max_length=250)

    def __str__(self):
        return self.title

class Information(models.Model):
    username = models.CharField(max_length=20)
    Firstname = models.CharField(max_length=20)
    Lastname = models.CharField(max_length=20)
    email = models.EmailField()
    #joindetail = models.DateTimeField('party date',default=datetime.datetime.now,blank=True,null=True)
    number = models.IntegerField(max_length=None)
    join = models.CharField(max_length=50)
    last_active = models.CharField(max_length =50)
    

    def __str__(self):
        return str(self.number)

class Feedback(models.Model):
    RATING_CHOICES = (
        (1, 'very bad'),
        (2, 'bad'),
        (3, 'fine'),
        (4, 'good'),
        (5, 'excellent'),
    )
    email = models.EmailField(max_length=20)
    website_rating = models.IntegerField(choices=RATING_CHOICES)
    artwork_rating = models.IntegerField(choices=RATING_CHOICES)
    youtube_rating = models.IntegerField(choices=RATING_CHOICES)
    feedback = models.CharField(max_length=200)



    
