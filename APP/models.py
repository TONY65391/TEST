from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    
    username = models.CharField(max_length=20)
    
    email = models.EmailField(unique=True)
    
    password = models.CharField(max_length=20)
    
    Profile_Picture = models.ImageField(default="", blank=False, null=False, upload_to='APP/static/users')
    
    