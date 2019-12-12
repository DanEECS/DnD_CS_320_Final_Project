from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def createAccount(request):
    if request.method == 'POST':
        registerform = UserCreationForm(request.POST)
        if registerform.is_valid():
            registerform.save()
            messages.success(request, f'Success! Your account has been created! You may now log in.')
            return redirect('login')
    else:
        registerform = UserCreationForm()
    return render(request, 'users/createAccount.html', {'form': registerform})
