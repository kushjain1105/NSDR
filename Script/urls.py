from django.urls import path
from . import views

app_name = "Script"

urlpatterns = [
    path("", views.index, name="index")
]
