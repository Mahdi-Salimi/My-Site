from django.contrib import admin
from django.urls import path

from . import views

app_name= 'website'

urlpatterns = [
    path('home/', views.blog_home, name='blog-home'),
    path('single/', views.blog_single, name='blog-single'),

]