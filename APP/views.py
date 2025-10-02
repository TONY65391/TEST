from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from . models import UserProfile
from . forms import SignupForm, LoginForm

# Create your views here.

def error(request):
    print(formhandler(request=request))
    return render(request, "error.html")

def home(request):
    return render(request, "home.html")

def signup(request):
    return render(request, "signup.html", {'signupform':SignupForm()})

def login(request):
    return render(request, "login.html", {'loginform':LoginForm()})

def formhandler(request):
    if request.POST and request.FILES:
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            return HttpResponse('Valid File')
        return render(request, "error.html", {'message':form.errors.as_text})