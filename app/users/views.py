from django.shortcuts import render, redirect
from .forms import *
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.contrib.auth.views import LoginView


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


class LoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    success_url = 'viewCharacters/'
    # username = super().request.user.username
