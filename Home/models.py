from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass


class School(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    image = models.URLField(blank=True)
    description = models.TextField(default="")
    def __str__(self):
        return f"About {self.name}"
    
    
class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    bio = models.TextField()
    image = models.ImageField(upload_to="images/")
    def __str__(self):
        return f"{self.user.first_name}'s Profile"
    