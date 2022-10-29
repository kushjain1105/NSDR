from django.db import models
from Home.models import User
# Create your models here.
class Report(models.Model):
    subject = models.ForeignKey(User, on_delete=models.CASCADE)
    graphURL = models.URLField()
    dateTime = models.DateTimeField()

    def __str__(self):
        return f"{self.subject}'s Report"