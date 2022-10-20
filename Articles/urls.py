from django.urls import path
from . import views

app_name = "Articles"

urlpatterns = [
    path("", views.index, name="index"),
    path("article/<title>", views.article, name="article"),
    path("create", views.create, name="create"),
    path("edit/<title>", views.edit, name="edit"),
    path("article/<title>/delete", views.delete, name="delete"),
]
