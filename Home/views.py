from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password, is_password_usable
from .models import *
# Create your views here.

def usernames():
    usernames = []
    for user in User.objects.all():
        usernames.append(user.username)
    return usernames

def index(request):
    return render(request, "Home/index.html")

def login_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("Home:index"))
        else:
            return render(request, "Home/login.html", {
                "message": "Invalid Credentials."
            })

    if request.user.is_authenticated:
        return render(request, 'Home/error.html', {
            "message": "You are already logged in."
        })
    return render(request, "Home/login.html")

def logout_request(request):
    logout(request)
    return HttpResponseRedirect(reverse("Home:index"))

def about(request):
    return render(request, "Home/about.html")

def register(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        firstName = request.POST["firstName"]
        lastName = request.POST["lastName"]
        email = request.POST["email"]

        previous_usernames = usernames()

        if not username or not password or not firstName or not lastName or not email:
            return render(request, "Home/register.html", {
                "message": "Incomplete Information."
            })        
            
        if username in previous_usernames:
            return render(request, "Home/register.html", {
                "message": "Username already exists."
            })        

        password = make_password(password)

        if not is_password_usable(password):
            return render(request, "Home/register.html", {
                "message": "Invalid Password."
            })        
        
        user = User(username=username, password=password, first_name=firstName, last_name=lastName, email=email)
        user.save()
        login(request, user)
        return HttpResponseRedirect(reverse("Home:index"))

    return render(request, "Home/register.html")

def form(request):
    if request.user.is_authenticated == False:
        return HttpResponseRedirect(reverse("Home:login"))
    return render(request, "Home/form.html")