from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404

def blog_home(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request,pid):
    # post = Post.objects.filter(pk = pid)
    post = get_object_or_404(Post, pk=pid , status=1)
    context = {'post': post}
    return render(request, 'blog/blog-single.html', context) 