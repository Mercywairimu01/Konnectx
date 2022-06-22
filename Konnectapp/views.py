from django.shortcuts import render,redirect
from .forms import *
from django.views.generic import CreateView
# Create your views here.

def register(request):
    return render(request,'registration/register.html')


class artist_register(CreateView):
    model=User
    form_class= ArtistSignUpForm
    template_name='registration/artist_register.html'
    
    
class distributor_register(CreateView):
    model=User
    form_class= DistributorSignUpForm
    template_name='registration/distributor_register.html'    