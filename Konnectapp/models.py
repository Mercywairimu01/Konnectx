from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Q
from django.core.validators import FileExtensionValidator
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

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
    video = models.FileField(upload_to='videos_uploaded/',null=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv','mp3'])])
    profile_image = models.ImageField(upload_to ='images/',default= 'default.jpg')
    country = models.CharField(max_length=25, blank=True)
    title = models.CharField(max_length= 200,null=True)
    email = models.EmailField(max_length=255, blank=True)
    website = models.URLField(max_length=250)    
    
    def __str__(self):
        return f'{self.user.username} profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()         



class DProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name_distributor = models.CharField(max_length=255, blank=True,null=True)
    image = models.ImageField(upload_to ='images/',default= 'default.jpg')
    location = models.CharField(max_length=25, blank=True)
    number = models.IntegerField(null=True)
    email = models.EmailField(max_length=255, blank=True)
    website = models.URLField(max_length=250)


    def __str__(self):
        return f'{self.user.username} dprofile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            DProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.dprofile.save()   