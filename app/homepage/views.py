from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import *
from django.views.generic import TemplateView, ListView
from .models import Character


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
			return redirect('classAndSpecialization')
		else:
			return render(request, 'CreateNewCharacter.html', {'form': form})
	return render(request, 'createNewCharacter.html')


class Manual(TemplateView):
	template_name = 'manual.html'


class StandardArray(TemplateView):
	template_name = 'standardArray.html'


class PointBuy(TemplateView):
	template_name = 'pointBuy.html'


class AddAttributes(TemplateView):
	template_name = 'addAttributes.html'


class ClassAndSpecialization(TemplateView):
	template_name = 'classAndSpecialization.html'


class CharDescription(TemplateView):
	template_name = 'charDescription.html'


class CharSkillsAndTraits(TemplateView):
	template_name = 'charSkillsTraits.html'


class Equipment(TemplateView):
	template_name = 'equipment.html'


class ViewCharacters(ListView):
	template_name = 'viewList.html'
	model = Character
	context_object_name = 'characters'
	ordering = ['date_made']
	# queryset = model.objects.filter('')
	paginate_by = 100  # if pagination is needed
	# user_characters = Character.objects.filter('')

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['now'] = timezone.now
		return context


class ViewCharacter(TemplateView):
	template_name = 'viewCharacter.html'


