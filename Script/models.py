from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class nsdr_type(models.Model):
    types = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.types}"
    
class Script(models.Model):
    audio = CloudinaryField("Audio", resource_type="auto")
    name = models.CharField(max_length=250)
    duration = models.DecimalField(max_digits=5, decimal_places=2)
    nsdr = models.ForeignKey(nsdr_type, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
    