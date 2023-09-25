from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger

def blog_home(request,cat_name=None, author_username=None):
    posts = Post.objects.all()
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    if author_username :
        posts = posts.filter(author__username=author_username)
        
    posts = Paginator(posts, 2)
    try:
        page_number =request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request,pid):
    # post = Post.objects.filter(pk = pid)
    post = get_object_or_404(Post, pk=pid , status=1)
    context = {'post': post}
    return render(request, 'blog/blog-single.html', context) 

def blog_search(request):
    posts = Post.objects.all()
    if request.method == 'GET':
        if search := request.GET.get('s'):
            posts = posts.filter(content__contains=search)
        # print(request.GET.get('s'))

    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)

    

# def blog_category(request, cat_name):
#     posts = Post.objects.filter(status=1)
#     posts = posts.filter(category__name=cat_name)
#     context = {'posts': posts}
#     return render(request, 'blog/blog-home.html', context)