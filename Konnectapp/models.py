from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
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
    role_artist = models.CharField(max_length=255, blank=True, null=True)
    profile_image = models.ImageField(upload_to ='images/',default= 'default.jpg')
    location = models.CharField(max_length=25, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    website = models.URLField(max_length=250)    

