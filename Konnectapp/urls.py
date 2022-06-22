from django.urls import path,include
from django.contrib.auth import views 
from . import views
from .views import *


urlpatterns = [
    path('', views.index, name="landingPage"),
    path('home/',views.home,name='home'),
    path('register/',views.register,name ='register'),
    path('artist_register/',views.artist_register.as_view(),name='artist_register'),
    path('distributor_register/',views.distributor_register.as_view(),name='distributor_register'),
    path('profile/<id>/',views.profile,name = 'profile'),
    path('profile/<username>/edit/', views.edit_profile, name='edit-profile'),
 

]