from django.urls import path
from . import views

app_name = "Home"

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("register", views.register, name="register"),
    path("about", views.about, name="about"),
    path("form", views.form, name="form"),
]
