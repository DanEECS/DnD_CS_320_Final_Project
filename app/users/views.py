from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import UserLoginForm


def login(request):
    if request.method == 'POST':
        registerform = UserCreationForm(request.POST)
        loginform = UserLoginForm(request.POST)
        if registerform.is_valid():
            if loginform.is_valid():
                messages.error(request, 'Please login OR sign up, not both!')
                return render(request, 'homepage/login.html', {'form': registerform, 'form': loginform})
            username = registerform.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('homepage')
        if loginform.is_valid():
            if registerform.is_valid():
                messages.error(request, 'Please login OR sign up, not both!')
                return render(request, 'homepage/login.html', {'form': registerform, 'form': loginform})


    else:
        registerform = UserCreationForm()
        loginform = UserLoginForm()
    return render(request, 'homepage/login.html', {'form': registerform, 'form': loginform})


