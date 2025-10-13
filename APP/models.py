from django.db import models
from django.core.validators import RegexValidator

# # Create your models here.

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    Profile_Picture = models.ImageField(default="", upload_to='APP/static/users')
    
    def __str__(self):
        return self.name
    

class Director(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    continent = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='APP/static/directors', null=True, blank=True)
    
    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    continent = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='APP/static/actors', null=True, blank=True)
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    duration = models.CharField(max_length=20)
    rating = models.FloatField()
    language = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    actors = models.ManyToManyField(Actor, through='MovieActor')
    picture = models.ImageField(upload_to='APP/static/movies', null=True, blank=True)
    
    def __str__(self):
        return self.title

class MovieActor(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    character = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='APP/static/movie-actor', null=True, blank=True)

