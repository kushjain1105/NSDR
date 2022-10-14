from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
# Create your views here.
def index(request):
    scripts = Script.objects.all()
    
    return render(request, "Script/index.html", {
        "scripts": scripts
    })