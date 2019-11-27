from django.shortcuts import render

def home(request):
	return render(request, 'homepage/index.html')


def login(request):
	return render(request, 'homepage/login.html')
