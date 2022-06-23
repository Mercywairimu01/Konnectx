from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.shortcuts import render,redirect,get_object_or_404
from .models import Profile
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.contrib import messages
from .forms import *

# Create your views here.

def index(request):
    '''
    View function that renders the landing page and its data
    '''
    return render(request, "index.html")
  
def home(request):
  
    return render(request,'home.html')
  

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'registration/register.html' ,{'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_artist:
                login(request, user)
                return redirect('home')
            elif user is not None and user.is_distributor:
                login(request, user)
                return redirect('home')
           
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'registration/login.html', {'form': form, 'msg': msg})

def contact(request):
    if request.method=="POST":
        contact=Contact()
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        contact.email=email
        contact.subject=subject
        contact.save()
        messages.success(request,"Inquiry received a response will be sent to your email")
        return redirect('home')

    return render(request, 'contact.html')    
    
def search_user(request):
  if 'search' in request.GET and request.GET['search']:
    search_term = request.GET.get('search')
    searchresults = User.search_user(search_term)
    return render(request, 'search.html', {'searchresults':searchresults, 'search_term':search_term})
  else:
    return redirect('home')
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