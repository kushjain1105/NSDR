from django.db import models
from django.contrib.auth.models import AbstractUser
import Home.models
# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("Home.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"Article: {self.title}"
    