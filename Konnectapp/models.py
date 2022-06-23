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
 

    