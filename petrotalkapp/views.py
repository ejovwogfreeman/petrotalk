from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import * 
from .models import *

# Create your views here.
def home_page(request):
    page='home_page'
    context = {
        'page': page
    }
    return render(request, 'pages/home.html', context)

def about_page(request):
    return render(request, 'pages/about.html')

def register_page(request):
    page='register_page'
    if request.user.is_authenticated:
        return redirect('profile_page')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'accouunt created for {user.username} succefully')
            return redirect('login_page')
    else:
        form = UserRegisterForm()
    context = {
        'page': page,
        'form': form
    }
    return render(request, 'pages/login_register.html', context)

def login_page(request):
    page='login_page'
    if request.user.is_authenticated:
        return redirect('profile_page')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'{user.username} logged in successfully')    
            if 'next' in request.GET:
                return redirect(request.GET.get('next'))
            else:
                return redirect('home_page')
    else:
        form = AuthenticationForm()
    context = {
        'page': page,
        'form': form
    }
    return render(request, 'pages/login_register.html', context)

def logout_page(request):
    logout(request)
    messages.warning(request, 'You have logged out, log in again to continue')
    return redirect('login_page')


@login_required(login_url="login_page")
def profile_page(request):
    return render(request, 'pages/profile.html')

@login_required(login_url="login_page")
def update_profile_page(request):
    if request.method=="POST":
        form = UserUpdateForm(request.POST, request.FILES, instance = request.user)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'accouunt updated for {user.username} successfully')
            return redirect('profile_page')
    else:
        form = UserUpdateForm(instance = request.user)
    context = {
        'form': form
    }
    return render(request, 'pages/profile_update.html', context)

def notfound_page(request, exception):
    return render(request, 'pages/notfound_page.html')