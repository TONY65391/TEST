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
        usernameExists = UserProfile.objects.filter(username = request.POST["username"]).exists()
        emailExists = UserProfile.objects.filter(email = request.POST["email"]).exists()
        form = SignupForm(request.POST, request.FILES)
        error = loader.get_template('error.html')
        if form.is_valid():
            profile = loader.get_template('profile.html')
            # if usernameExists and emailExists:
            #     context = {'message': "Username and Email already exists"}
            #     return HttpResponse(error.render(request=request, context=context))
            # elif usernameExists == False and emailExists:
            #     context = {'message': "Email already exists"}
            #     return HttpResponse(error.render(request=request, context=context))
            # elif usernameExists and emailExists == False:
            #     context = {'message': "Username already exists"}
            #     return HttpResponse(error.render(request=request, context=context))
            # if usernameExists or emailExists:
            #     return HttpResponseRedirect(request, "signup.html", {'message':form.errors})
            # else:
            form.save()
            return redirect("login")
        context = {'message':form.errors.as_text()}
        return HttpResponse(error.render(request=request, context=context))
