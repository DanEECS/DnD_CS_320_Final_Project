from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def home(request):
	return render(request, 'homepage/index.html')


def login(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!')
			return redirect('homepage')
	else:
		form = UserCreationForm()
	return render(request, 'homepage/login.html', {'form': form})
