from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm,CustomAuthenticationForm
from django.contrib.auth.models import User

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            for item in User.objects.all():
                    if item.email == request.POST.get('username'):
                        email = item.username
    
            form = AuthenticationForm(request=request, data=request.POST)
            print(form.data)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None :
                    login(request, user)
                    return redirect('/')
            else:
                password = form.data['password'] 
                user = authenticate(request, username=email, password=password)
                login(request, user)
                return redirect('/')
                
                                     
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('/')
    
@login_required()
def logout_view(request):

    logout(request)
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            request.user.email = request.POST.get('email')
            if form.is_valid():
                form.save()
                return redirect('/')
        form = CustomUserCreationForm()
        context = {'form':form}
        return render (request, 'accounts/signup.html', context)
    else:
        return redirect('/')
   
    
    
    

