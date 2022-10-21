from django.shortcuts import render
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