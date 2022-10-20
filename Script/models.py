from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class nsdr(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Script(models.Model):
    audio = CloudinaryField("Audio", resource_type="auto")
    name = models.CharField(max_length=250)
    duration = models.DecimalField(max_digits=5, decimal_places=2)
    # nsdrType = models.ForeignKey(nsdr_type, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"    