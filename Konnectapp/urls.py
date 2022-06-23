from django.urls import path,include
from django.contrib.auth import views 
from . import views
from .views import *


urlpatterns = [
    path('', views.index, name="landingPage"),
    path('home/',views.home,name='home'),
    path('logout/',views.logoutUser,name='logout'),
    path('explore/',views.explore,name ='explore'),
    path('register/',views.register,name ='register'),
    path('login/', views.login_view, name='login'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'), 
    path('search/', views.search_user, name='search'),
    path('profile/<username>/',views.profile,name = 'profile'),
    path('distributor_profile/<username>/',views.dprofile,name = 'distributor_profile'),

 

]