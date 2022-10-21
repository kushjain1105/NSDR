from django.urls import path
from . import views

app_name = "Research"

urlpatterns = [
    path("", views.index, name="index"),
    path("project/<title>", views.load_project, name="project"),
    path("project/paper/<id>", views.load_paper, name="paper"),
    path("project/images/<project_title>", views.load_images, name="images"),
]
