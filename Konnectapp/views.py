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


def profile(request, username):
    images = request.user.profile
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    params = {
        'user_form': user_form,
        'prof_form': prof_form,
        'images': images,

    }
    return render(request, 'konnectx/profile.html', params)


def user_profile(request, username):
    user_prof = get_object_or_404(User, username=username)
    if request.user == user_prof:
        return redirect('profile', username=request.user.username)
    user_posts = user_prof.profile.post.all()
    
    params = {
        'user_prof': user_prof,
        'user_posts': user_posts,
    }
    return render(request, 'konnectx/user_profile.html', params)
