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
    path("about/<user>", views.member, name="member"),
    path("schools", views.schools, name="schools"),
    path("sources", views.sources, name="sources"),
    path("documentation", views.documentation, name="documentation"),
    path("contact", views.contact, name="contact"),
    path("change_profile", views.change_profile, name="change_profile"),
    path("add_sources", views.add_sources, name="add_sources"),
]