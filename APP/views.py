from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from django.template.context_processors import request
from . models import UserProfile, Movie, MovieActor
from . forms import SignupForm, LoginForm

# Create your views here.

def error(request):
    return render(request, "error.html")

def home(request):
    return render(request, "home.html")

def signup(request):
    return render(request, "signup.html", {'signupform':SignupForm()})

def login(request):
    return render(request, "login.html", {'loginform':LoginForm()})

def movie_details(request, movie_id):
    template = loader.get_template('movie_details')
    return HttpResponse(template.render(request=request))



def formhandler(request):
    if request.POST and request.FILES:
        usernameExists = UserProfile.objects.filter(username = request.POST["username"]).exists()
        emailExists = UserProfile.objects.filter(email = request.POST["email"]).exists()
        passwordExists = UserProfile.objects.filter(password = request.POST["password"]).exists()
        form = SignupForm(request.POST, request.FILES)
        error = loader.get_template('error.html')
        
        if usernameExists or emailExists or passwordExists:
            context = {'message' : 'Username or password or email already exists'}
            return HttpResponse(error.render(request=request, context=context))
        else:
            if form.is_valid():
                form.save()
                return redirect("login")
            else:
                context = {'message' : form.errors}
                return HttpResponse(error.render(request=request, context=context))
        
    elif request.GET:
        try:
            user = UserProfile.objects.get(username = request.GET["username"]) and UserProfile.objects.get(password = request.GET["password"])
            template = loader.get_template('profile.html')
            context = {
                'user':user,
                'movies':Movie.objects.prefetch_related().all()}
            return HttpResponse(template.render(request=request, context=context))
        except:
            template = loader.get_template('error.html')
            context = {'message' : 'Username or password does not exist', 'path':'signup'}
            return HttpResponse(template.render(request=request, context=context))
        
