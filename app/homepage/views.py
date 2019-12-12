from django.shortcuts import render, redirect
from .forms import *
from django.views.generic import TemplateView, ListView


class Home(TemplateView):
	template_name = 'index.html'


class About(TemplateView):
	template_name = 'about.html'


class Help(TemplateView):
	template_name = 'help.html'


def CreateCharacter(request):
	if request.method == 'POST':
		form = CharacterIdentityForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('addAttributes')
		else:
			return render(request, 'classAndSpecialization.html', {'form': form})
	return render(request, 'classAndSpecialization.html')



class Manual(TemplateView):
	template_name = 'manual.html'


class StandardArray(TemplateView):
	template_name = 'standardArray.html'


class PointBuy(TemplateView):
	template_name = 'pointBuy.html'


class AddAttributes(TemplateView):
	template_name = 'addAttributes.html'


class CharDescription(TemplateView):
	template_name = 'charDescription.html'


class Equipment(TemplateView):
	template_name = 'equipment.html'


class ViewCharacters(TemplateView):
	template_name = 'viewCharacterList.html'
