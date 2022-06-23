from django.shortcuts import render,redirect,get_object_or_404
from .models import Profile
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import *
from django.views.generic import CreateView

# Create your views here.

def index(request):
    '''
    View function that renders the landing page and its data
    '''
    return render(request, "index.html")
  
def home(request):
  
    return render(request,'home.html')
  
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

def profile(request,username):
  '''
  View function that renders the profile page and its data
  '''

  user_info_form = UpdateUserInfoForm()
  update_profile_form = UpdateProfileForm()
  
  if request.method == 'POST':
    user_info_form = UpdateUserInfoForm(request.POST,instance=request.user)
    update_profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
    
    if user_info_form.is_valid and update_profile_form.is_valid():
            user_info_form.save()
            update_profile_form.save()
            return HttpResponseRedirect(request.path_info)
  else:
        user_info_form = UpdateUserInfoForm(instance=request.user)
        update_profile_form = UpdateProfileForm(instance=request.user.profile)
  return render(request, 'konnectx/profile.html', locals())

def edit_profile(request,username):
    use = User.objects.get(username=username)
    if request.method == 'POST':
        return redirect('profile',request.user.username)
    return render(request, 'konnectx/profile.html')
