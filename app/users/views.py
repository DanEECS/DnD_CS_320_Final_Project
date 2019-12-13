from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages


def createAccount(request):
    if request.method == 'POST':
        registerform = CreateAccountForm(request.POST)
        if registerform.is_valid():
            registerform.save()
            messages.success(request, 'Success! Your account has been created! You may now log in.')
            return redirect('login')
    else:
        registerform = CreateAccountForm()
    return render(request, 'users/createAccount.html', {'form': registerform})


def Login(request):
    if request.method == 'POST':
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            username = loginform.cleaned_data.get('username')
            loginform.save()
            messages.success(request, f'Welcome back {username}!')
            return redirect('viewCharacters')
    else:
        loginform = LoginForm()
    return render(request, 'users/login.html', {'form': loginform})
