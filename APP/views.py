from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from . models import UserProfile
from . forms import SignupForm

# Create your views here.

def signup(request):
    return render(request, "signup.html", {'signupform':SignupForm()})