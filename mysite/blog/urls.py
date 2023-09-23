from django.contrib import admin
from django.urls import path

from . import views

app_name= 'blog'

urlpatterns = [
    path('', views.blog_home, name='blog-home'),
    path('<int:pid>/', views.blog_single, name='blog-single'),

]