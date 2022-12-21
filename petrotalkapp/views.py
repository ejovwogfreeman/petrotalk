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
    rooms = Room.objects.all()
    context = {
        'page': page,
        'rooms': rooms
    }
    return render(request, 'pages/home.html', context)

def topics(request):
    return {
        'topics' : Topic.objects.all()
    }

def room_page(request, pk):
    room = Room.objects.get(id=pk)
    context = {
        'room': room
    }
    return render(request, 'pages/room.html', context)

@login_required(login_url="login_page")
def create_room_page(request):
    page="create_room_page"
    if request.method == "POST":
        form = CreateRoomForm(data=request.POST)
        if form.is_valid:
            room = form.save(commit = False)
            room.author = request.user
            room.save()
        messages.success(request, f'room "{room.name}" created successfully')
        return redirect('home_page')
    else:
        form = CreateRoomForm()

    context = {
        'page': page,
        'form': form
    }
    return render(request, 'pages/create_update.html', context)

@login_required(login_url="login_page")
def update_room_page(request, pk):
    page = "update_room_page"
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        form = UpdateRoomForm(instance = room, data=request.POST)
        if form.is_valid:
            room = form.save(commit = False)
            room.author = request.user
            room.save()
        messages.success(request, f'room {room.name} updated successfully')
        return redirect('home_page')
    else:
        form = UpdateRoomForm(instance = room)

    context = {
        'page': page,
        'form': form
    }
    return render(request, 'pages/create_update.html', context)

@login_required(login_url="login_page")
def delete_room_page(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        messages.warning(request, f'room "{room.name}" deleted successfully')
        return redirect('home_page')
    return render(request, 'pages/delete.html', {'obj': room})
    context = {
        'obj': room
    }
    return render(request, 'pages/delete.html', context)

def register_page(request):
    page='register_page'
    if request.user.is_authenticated:
        return redirect('profile_page')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'accouunt created for {user.username} successfully')
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
def profile_page(request, pk):
    user = User.objects.get(username=pk)
    rooms = Room.objects.all()
    context = {
        'user': user,
        'rooms': rooms
    }
    return render(request, 'pages/profile.html', context)

@login_required(login_url="login_page")
def update_profile_page(request):
    if request.method=="POST":
        form = UserUpdateForm(request.POST, request.FILES, instance = request.user)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'accouunt updated for {user.username} successfully')
            return redirect('profile_page', pk=user.username)
    else:
        form = UserUpdateForm(instance = request.user)
    context = {
        'form': form
    }
    return render(request, 'pages/profile_update.html', context)

def notfound_page(request, exception):
    return render(request, 'pages/notfound_page.html')