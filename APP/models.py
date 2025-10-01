from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    
    username = models.CharField(max_length=20, validators=[RegexValidator(regex=r'^[a-zA-Z0-9_]*$', message='Username can only contain letters, numbers, and underscores \nHint: @/[1-10][a-z][A-Z]', code='Invalid Username')])
    
    email = models.EmailField(unique=True)
    
    password = models.CharField(max_length=20, validators=[RegexValidator(regex=r'^[a-zA-Z0-9_]*$', message='Password can only contain letters, numbers, and underscores.\nHint: @/[1-10][a-z][A-Z]', code='Invalid Password')])
    
    Profile_Picture = models.ImageField(default="", blank=False, null=False, upload_to='APP/static/users')
    
    