from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.contrib.auth import login, logout
from django.contrib import messages

# Create your views here.
def home_page(request):
    return render(request, 'pages/home.html')

def about_page(request):
    return render(request, 'pages/about.html')

def register_page(request):
    page='register_page'
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # messages.success(request, f'accouunt created for {user.username} succefully')
            print(f'account created for {user.username}')
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
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
             # messages.success(request, f'{user.username} logged in successfully')
            print(f'{user.username} logged in successfully')        
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
    return redirect('login_page')


