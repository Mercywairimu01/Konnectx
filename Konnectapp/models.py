from django.db import models
from django.contrib.auth.models import AbstractUser
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