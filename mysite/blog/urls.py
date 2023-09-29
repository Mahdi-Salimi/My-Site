from django.contrib import admin
from django.urls import path,include
from blog.feeds import LatestEntriesFeed

from . import views

app_name= 'blog'

urlpatterns = [
    path('', views.blog_home, name='blog-home'),
    path('<int:pid>/', views.blog_single, name='blog-single'),
    path('category/<str:cat_name>/', views.blog_home, name='blog-category'),
    path('tag/<str:tag_name>/', views.blog_home, name='blog-tag'),
    path('author/<str:author_username>/', views.blog_home, name='author'),
    path('search/', views.blog_search, name='blog-search'),
    path('rss/feed/', LatestEntriesFeed()),
  ]