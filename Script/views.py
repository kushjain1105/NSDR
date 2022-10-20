from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
# Create your views here.
def sortScripts():
    scripts = Script.objects.all()
    scriptNames = []
    for script in scripts:
        scriptNames.append(script.name)
    scriptNames.sort()

    scriptObjects = []
    for script in scriptNames:
        scriptObjects.append(Script.objects.get(name=script))
    return scriptObjects

def index(request):
    scripts = sortScripts()
    
    return render(request, "Script/index.html", {
        "scripts": scripts
    })