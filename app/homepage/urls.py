from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
    path('help/', Help.as_view(), name='help'),
    path('createCharacter/', views.CreateCharacter, name='createCharacter'),
    path('classAndSpecialization/', ClassAndSpecialization.as_view(), name='classAndSpecialization'),
    path('addAttributes/', AddAttributes.as_view(), name='addAttributes'),
    path('addAttributes/manual/', Manual.as_view(), name='manual'),
    path('addAttributes/standard/', StandardArray.as_view(), name='standard'),
    path('addAttributes/pointBuy', PointBuy.as_view(), name='pointBuy'),
    path('characterDescription/', CharDescription.as_view(), name='charDescription'),
    path('skillsAndTraits/', CharSkillsAndTraits.as_view(), name='charSkillsTraits'),
    path('equipment/', Equipment.as_view(), name='equipment'),
    path('viewCharacters/', ViewCharacters.as_view(), name='viewCharacters'),
    path('viewCharacter/', ViewCharacter.as_view(), name='viewCharacter'),
]
