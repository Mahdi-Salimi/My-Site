from django.shortcuts import render
from .models import Post, Comment
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from blog.forms import CommentForm
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse 
from django.http import HttpResponseRedirect


def blog_home(request,cat_name=None, author_username=None, tag_name=None):
    posts = Post.objects.all()
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    if author_username :
        posts = posts.filter(author__username=author_username)
    if tag_name :
        posts = posts.filter(tag__name=tag_name)
        
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
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Your comment submitted successfully')
        else:
            messages.add_message(request,messages.ERROR,'Your comment submitted successfully')
            
    post = get_object_or_404(Post, pk=pid , status=1)
    post.counted_views = post.counted_views + 1
    post.save()
    
    if not post.login_require:
        comments = Comment.objects.filter(post = post.id, approved=True)
        form = CommentForm()
        context = {'post': post, 'comments': comments, 'form': form}
        return render(request, 'blog/blog-single.html', context) 
    else:
        return HttpResponseRedirect(reverse('accounts:login'))

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