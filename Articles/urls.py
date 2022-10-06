from django.urls import path
from . import views

app_name = "Articles"

urlpatterns = [
    path("", views.index, name="index"),
    path("/article/<title>", views.article, name="article"),
]
