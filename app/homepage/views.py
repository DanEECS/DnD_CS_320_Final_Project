from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class Home(TemplateView):
	template_name = 'index.html'


class About(TemplateView):
	template_name = 'about.html'


class Help(TemplateView):
	template_name = 'help.html'
