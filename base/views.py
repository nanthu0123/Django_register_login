from django.contrib.messages.storage.base import Message
from django.http import request
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


def home(request):
    return render(request, 'home.html')


def register(request):
    form = UserRegisterForm
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            userName = form.cleaned_data.get('username')
            messages.success(request, f'account created for {userName}')
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'entry does not exist')

    return render(request, 'login.html')

def logout(request):
        auth_logout(request)
        messages.info(request,'logout successfully')
        return redirect('login')

