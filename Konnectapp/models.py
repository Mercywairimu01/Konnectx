from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Q
# Create your models here.

class User(AbstractUser):
    is_artist = models.BooleanField('An artist', default=False)
    is_distributor = models.BooleanField('A distributor',default=False)

    @classmethod
    def search_user(cls, searchterm):
        searchresults = cls.objects.filter(Q(is_artist__icontains=searchterm) | Q(is_distributor__icontains=searchterm))
        return searchresults


class Contact(models.Model):
    email=models.EmailField()   
    subject=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name_artist = models.CharField(max_length=255, blank=True,null=True)
    role_artist = models.CharField(max_length=255, blank=True, null=True)
    profile_image = models.ImageField(upload_to ='images/',default= 'default-img.jpg')
    location = models.CharField(max_length=25, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    website = models.URLField(max_length=250)    


