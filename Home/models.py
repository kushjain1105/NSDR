from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from Articles.models import *

# Create your models here.
class User(AbstractUser):
    pass

class School(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField()
    image = models.URLField(blank=True)
    description = models.TextField(default="")

    def __str__(self):
        return f"School: {self.name}"
        
class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)
    bio = models.TextField()
    member_image = models.ImageField(upload_to="images/", blank=True)
    teacher = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.first_name}'s Profile"