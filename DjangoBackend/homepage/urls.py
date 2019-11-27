from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage-home'),
    path('login', views.login, name='homepage-login')

]