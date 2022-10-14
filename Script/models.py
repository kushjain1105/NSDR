from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class NSDR(models.Model):
    NSDRType = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.NSDRType}"
    
class Script(models.Model):
    audio = CloudinaryField("Audio", resource_type="auto")
    name = models.CharField(max_length=250)
    duration = models.DecimalField(max_digits=5, decimal_places=2)
    Type = models.ForeignKey(NSDR, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
    