from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
    path('help/', Help.as_view(), name='help')
]
