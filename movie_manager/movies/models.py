from django.db import models

# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=300)
    def __str__(self):
        return self.name


class CensorInfo(models.Model):
    rating=models.CharField(max_length=10)
    certified_by=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.rating

class Actor(models.Model):
    name = models.CharField(max_length=300)
    def __str__(self):
        return self.name


class MovieInfo(models.Model):
    title=models.CharField(max_length=250)
    year = models.IntegerField(null=True)
    summary = models.TextField()
    poster=models.ImageField(upload_to='images/',null=True)
    censor_details = models.ForeignKey(CensorInfo,on_delete=models.CASCADE,related_name='movie',null=True)
    director=models.ForeignKey(Director, on_delete=models.CASCADE,null=True,related_name='directed_movies')
    actor=models.ManyToManyField(Actor)
    
    def __str__(self):
        return self.title