from django.urls import path
from . import views

app_name = "Dashboard"

urlpatterns = [
    path("", views.index, name="index"),
    path("previous_reports", views.previous_reports, name="previous_reports")
]
