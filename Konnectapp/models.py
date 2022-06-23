from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.

class User(AbstractUser):
    is_artist = models.BooleanField(default=False)
    is_distributor = models.BooleanField(default=False)
    full_name =models.CharField(max_length= 200,null=True)
    
    
class Artist(models.Model):  
    user =models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    location = models.CharField(max_length= 200,null=True)  
    
class Distributor(models.Model):  
    user =models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    location = models.CharField(max_length= 200,null=True)  
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name_artist = models.CharField(max_length=255, blank=True,null=True)
    video = models.FileField(upload_to='videos_uploaded',null=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv','mp3'])])
    profile_image = models.ImageField(upload_to ='images/',default= 'default.jpg')
    country = models.CharField(max_length=25, blank=True)
    title = models.CharField(max_length= 200,null=True)
    email = models.EmailField(max_length=255, blank=True)
    website = models.URLField(max_length=250)    
    
    def __str__(self):
        return self.title

