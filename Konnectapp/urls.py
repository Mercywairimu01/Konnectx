from django import views
from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name="landingPage"),
  path('test/', views.test, name="testPage"),
]