from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password, is_password_usable
from django.template.defaultfilters import slugify
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
    schools = School.objects.all()
    members = Member.objects.all()
    students_list = []
    teachers_list = []

    # Filling members_list
    for member in members:
        if member.teacher == False:
            students_list.append(member)
        else:
            teachers_list.append(member)
    students_list.sort(key=lambda member:member.user.first_name)
    teachers_list.sort(key=lambda member:member.user.first_name)
    members_list = teachers_list + students_list
    return render(request, "Home/about.html", {
        "schools": schools,
        "members": members_list
    })

def member(request, user):
    member_user = User.objects.get(username=user)
    member_object = Member.objects.filter(user=member_user).first()
    # print(memvb)
    return render(request, "Home/member.html", {
        "member": member_object
    })

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

def members():
    membrs = Member.objects.all()
    users = []
    for member in membrs:
        users.append(member.user)
    return users

def form(request):

    if request.method == "POST":
        if request.user.is_authenticated == False:
            return render(request, "Home/form.html", {
                "message": "Please login/register first."
            })

        # If the user has already filled the form
        user = User.objects.get(username=request.user)
        member_users = members()
        if user in member_users:
            return render(request, "Home/form.html", {
                "message": "You have already submitted the form."
            })

        # If everything went well...
        school = request.POST["school"]
        school = School.objects.get(name=school)      
        bio = request.POST["bio"]
        image = request.FILES.get("image")
        m = Member(user=user, school=school, bio=bio, member_image=image)
        m.save()

        #If the user skipped some detail...
        if not bio or not image or not school:
            return render(request, "Home/form.html", {
                "message": "Please fill in the details."
            })

        return HttpResponseRedirect(reverse("Home:about"))

    # If request.method == "GET"...
    schools = School.objects.all()
    return render(request, "Home/form.html", {
        "schools": schools
    })


def schools(request):
    schools = School.objects.all()
    return render(request, "Home/schools.html", {
        "schools": schools
    })

def contact(request):
    users = User.objects.all()
    project_members = []
    members = Member.objects.all()
    member_users = []
    for member in members:
        member_users.append(member.user)
    for user in users:
        if user.is_staff:
            project_members.append(user)
    return render(request, "Home/contact.html", {
        "users": project_members,
        "members": member_users
    })

def documentation(request):
    return render(request, "Home/Documentation.html")
    
def sources(request):
    return render(request, "Home/Sources.html")

def research(request):
    return render(request, "Home/Research.html")

def outreach(request):
    return render(request, "Home/outreach.html")