from django.urls import path
from . import views

app_name = "Research"

urlpatterns = [
    path("", views.index, name="index")
]
