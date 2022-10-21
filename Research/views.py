from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
# Create your views here.
def index(request):
    projects = Project.objects.all()
    return render(request, "Research/index.html", {
        "projects": projects
    })

def load_project(request, title):
    project = Project.objects.get(title=title)
    papers = Paper.objects.filter(project=project)
    return render(request, "Research/project.html", {
        "project": project,
        "papers": papers
    })

def load_paper(request, id):
    paper = Paper.objects.get(pk=id)
    return render(request, "Research/paper.html",{
        "paper": paper
    })


def load_images(request, project_title):
    project = Project.objects.get(title=project_title)
    images = Image.objects.filter(project=project)
    return render(request, "Research/images.html", {
        "images": images
    })

def outreach(request):
    institutions = Institution.objects.all()
    return render(request, "Research/outreach.html", {
        "institutions": institutions
    })

def add_outreach(request):
    if request.method == "POST":
        name = request.POST["name"]
        address = request.POST["address"]
        imageURL = request.POST["imageURL"]
        description = request.POST["description"]

        if not name or not address or not imageURL or not description:
            return render(request, "Research/add_outreach.html", {
                "message": "Please fill in the details."
            })
        
        I = Institution(name=name, address=address,image=null, imageURL=imageURL, description=description)
        I.save()
        return HttpResponseRedirect(reverse("Research:outreach"))
    return render(request, "Research/add_outreach.html")