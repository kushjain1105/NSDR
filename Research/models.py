from django.db import models
from Home.models import Member
import datetime
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
    date = models.DateField(default=datetime.datetime.today())
    def __str__(self):
        return f"Research Paper: {self.title}"

class Image(models.Model):
    image = models.ImageField(upload_to="images/", blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    

class Institution(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    image = models.ImageField(upload_to="outreach/", blank=True)
    description = models.TextField()

    def __str__(self):
        return f"Outreach: {self.name}"
    
