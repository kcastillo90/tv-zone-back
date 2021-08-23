from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Shows(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    cast = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    avg_rating = models.CharField(max_length=50)
    year = models.CharField(max_length=20)
    video = models.URLField(max_length=200)
    added_by = ArrayField(models.CharField(max_length=200, blank=True))
    user_ratings = ArrayField(models.CharField(max_length=200, blank=True))
    user_reviews =  ArrayField(models.CharField(max_length=200, blank=True))

class Users(models.Model):
    username = models.CharField(max_length=75, unique=True)
    password = models.CharField(max_length=10000)
    # reviews = ArrayField(models.CharField(max_length=200, blank=True))
