from django.contrib import admin
from django.contrib.auth.models import User, Group
from . models import UserProfile
from . models import UserProfile

# Register your models here.
admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'username', 'email', 'password',]