from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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
      
class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')

class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name_artist', 'profile_image', 'location','role_artist','website']
    


# class ProfileForm(forms.ModelForm):
#     distributor_name = forms.CharField(max_length=255)
#     location = forms.CharField(max_length=50)
#     contact = forms.EmailField(max_length=250)
#     social_link = forms.URLField(max_length=255)

#     class Meta:
#         model = DProfile
#         fields = '__all__'
#         exclude = ['user']


class UpdateDUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

class UpdateDUserInfoForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'email')
        
class UpdateDProfileForm(forms.ModelForm):
    class Meta:
        model = DProfile
        fields = '__all__'