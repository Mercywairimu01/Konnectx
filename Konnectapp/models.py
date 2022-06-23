from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# from django.utils.translation import gettext as _
# from django.conf.urls.static import static
# from django.core.validators import FileExtensionValidator
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
    profile_image = models.ImageField(upload_to ='images/',default= 'default-img.jpg')
    location = models.CharField(max_length=25, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    website = models.URLField(max_length=250)    



# class DProfile(models.Model):
#     user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
#     avatar = models.ImageField(upload_to="images/", null=True, blank=True)
#     distributor_name = models.CharField(max_length=255, blank=True,null=True)
#     distributor_role = models.CharField(max_length=255, blank=True,null=True)
#     number = models.CharField(max_length=32, null=True, blank=True)
#     location = models.CharField(max_length=50, null=True, blank=True)
#     contact = models.CharField(max_length=255, null=True, blank=True)
#     social_link = models.CharField(max_length=255, null=True, blank=True)

#     def __str__(self):
#         return self.title

class DProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name_distributor = models.CharField(max_length=255, blank=True,null=True)
    p_image = models.ImageField(upload_to ='images/',default= 'default.jpg')
    locale = models.CharField(max_length=25, blank=True)
    title = models.CharField(max_length= 200,null=True)
    contact = models.EmailField(max_length=255, blank=True)
    social_link = models.URLField(max_length=250)    
    
    def __str__(self):
        return self.title