from importlib.metadata import distribution
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import *


class ArtistSignUpForm(UserCreationForm):
    full_name =  forms.CharField(required=True)
    location =  forms.CharField(required=True)
    
    
    class Meta(UserCreationForm.Meta):
        model= User
        
    @transaction.atomic
    def data_save(self):
        user=super().save(commit=False)  
        user.full_name =self.cleaned_data.get('full_name')
        user.save()
        artist  = Artist.objects.create(user=user)
        artist.location =self.cleaned_data.get('location')
        artist.save()
        return user
        
class DistributorSignUpForm(UserCreationForm):
    full_name =  forms.CharField(required=True)
    location =  forms.CharField(required=True)
    
    
    class Meta(UserCreationForm.Meta):
        model= User
       
    @transaction.atomic
    def data_save(self):
        user=super().save(commit=False)  
        user.full_name =self.cleaned_data.get('full_name')
        user.save()
        distributor  = Distributor.objects.create(user=user)
        distributor .location =self.cleaned_data.get('location')
        distributor.save() 
        return user 
    