from django.db import models
from Home.models import Member
# Create your models here.
class Project(models.Model):
    # Add date to project Field
    title = models.CharField(max_length=150)
    members = models.ManyToManyField(Member, related_name="projects")

    def __str__(self):
        return f"Research Project: {self.title}"

class Paper(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"Research Paper: {self.title}"

class Image(models.Model):
    image = models.ImageField("images/", blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    

