from django.db import models

# Create your models here.

class Picture(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='face/',null=True,blank=True)
    """   photo_name = models.CharField(max_length= 255)
    """
    def __str__(self):
        return self.name
   
