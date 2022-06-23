
from django.shortcuts import render,redirect,get_object_or_404
from .models import Profile, DProfile
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import *
# from .forms import ProfileForm, form_validation_error
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
from django.views.generic import CreateView
# from django.contrib import messages
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

def profile(request, username):
    images = request.user.profile
    if request.method == 'POST':
        user_form = UpdateDUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateDUserForm(instance=request.user)
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


# @method_decorator(login_required(login_url='login'), name='dispatch')
# class ProfileView(View):
#     profile = None

#     def dispatch(self, request, *args, **kwargs):
#         self.profile, __ = Profile.objects.get_or_create(user=request.user)
#         return super(ProfileView, self).dispatch(request, *args, **kwargs)

#     def get(self, request):
#         context = {'profile': self.profile, 'segment': 'profile'}
#         return render(request, 'konnectx/distributor_profile.html', context)

#     def post(self, request):
#         form = ProfileForm(request.POST, request.FILES, instance=self.profile)

#         if form.is_valid():
#             profile = form.save()
#             profile.user.name = form.cleaned_data.get('name')
#             profile.user.location = form.cleaned_data.get('location')
#             profile.user.contact = form.cleaned_data.get('location')
#             profile.user.email = form.cleaned_data.get('email')
#             profile.user.socail_link = form.cleaned_data.get('social-link')
#             profile.user.save()

#             messages.success(request, 'Profile saved successfully')
#         else:
#             messages.error(request, form_validation_error(form))
#         return redirect('profile')


def dprofile(request,username):
  '''
  View function that renders the profile page and its data
  '''

  user_info_form = UpdateDUserInfoForm()
  update_profile_form = UpdateDProfileForm()
  
  if request.method == 'POST':
    user_info_form = UpdateDUserInfoForm(request.POST,instance=request.user)
    update_profile_form = UpdateDProfileForm(request.POST, request.FILES, instance=request.user.profile)
    
    if user_info_form.is_valid and update_profile_form.is_valid():
            user_info_form.save()
            update_profile_form.save()
            return HttpResponseRedirect(request.path_info)
  else:
        user_info_form = UpdateDUserInfoForm(instance=request.user)
        update_profile_form = UpdateDProfileForm(instance=request.user.profile)
  return render(request, 'konnectx/distributor_profile.html', locals())

def edit_dprofile(request,username):
    use = User.objects.get(username=username)
    if request.method == 'POST':
        return redirect('distributor_profile',request.user.username)
    return render(request, 'konnectx/distributor_profile.html')