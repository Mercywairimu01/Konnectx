from django.shortcuts import render,redirect,get_object_or_404
from .forms import UpdateUserForm,UpdateUserProfileForm
from .models import Profile
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.

def profile(request, username):
    images = request.user.profile.post.all()
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
