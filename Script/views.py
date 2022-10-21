from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.

def f(script):
    script_list = script.split()
    return int(script_list[1])
def sortScripts():
    scripts_query_set = Script.objects.all()
    script_numbers = []
    scripts_list = []
    
    for script in scripts_query_set:
        scripts_list.append(script.name)

    scripts_list.sort(key=f)
    script_objects = []

    for script in scripts_list:
        script_item = Script.objects.get(name=script)
        script_objects.append(script_item)
    return script_objects

def index(request):
    scripts = sortScripts()
    
    return render(request, "Script/index.html", {
        "scripts": scripts
    })