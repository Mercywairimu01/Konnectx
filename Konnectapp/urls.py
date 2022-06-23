from django.urls import path,include
from django.contrib.auth import views 
from . import views
from .views import *


urlpatterns = [
    path('', views.index, name="landingPage"),
    path('home/',views.home,name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search_user, name='search'),
    path('profile/<username>/',views.profile,name = 'profile'),
]