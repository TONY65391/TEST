from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from . models import UserProfile
from . forms import SignupForm, LoginForm

# Create your views here.

def home(request):
    return render(request, "home.html")

def signup(request):
    return render(request, "signup.html", {'signupform':SignupForm()})

def login(request):
    return render(request, "login.html", {'loginform':LoginForm()})