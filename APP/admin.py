from django.contrib import admin
from django.contrib.auth.models import User, Group
from . models import Movie, Director, Actor, UserProfile, MovieActor

# Register your models here.
admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(MovieActor)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['movie', 'actor', 'role', 'character', 'picture']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'username', 'email', 'password']

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'release_date', 'description', 'director']
