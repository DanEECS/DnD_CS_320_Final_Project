from django import forms
from .models import Character


class CharacterIdentityForm(forms.ModelForm):
    characterName = forms.CharField(max_length=52)
    playerName = forms.CharField(max_length=52)
    Class = forms.TextInput()
    race = forms.TextInput()
    background = forms.TextInput()
    level = forms.NumberInput()
    alignment = forms.TextInput()
    experience = forms.NumberInput()

    class Meta:
        model = Character
        fields = ["characterName", "playerName", "level", "alignment", "experience"]
        widgets = {'Class': forms.TextInput(attrs={
            "_style": "search_multiple", "_override": "Select"
        }), 'race': forms.TextInput(attrs={
            "_style": "search_multiple", "_override": "Select"
        }), "background": forms.TextInput(attrs={
            "_style": "search_multiple", "_override": "Select"
        })}


class ManualCharacterAttributesForm(forms.ModelForm):
    strength = forms.IntegerField(widget=forms.NumberInput())
    dexterity = forms.IntegerField(widget=forms.NumberInput())
    constitution = forms.IntegerField(widget=forms.NumberInput())
    intelligence = forms.IntegerField(widget=forms.NumberInput())
    wisdom = forms.IntegerField(widget=forms.NumberInput())
    charm = forms.IntegerField(widget=forms.NumberInput())

    strengthMod = 0
    dexterityMod = 0
    constitutionMod = 0
    intelligenceMod = 0
    wisdomMod = 0
    charmMod = 0

    class Meta:
        model = Character
        fields = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charm']

    def clean(self):
        cleaned_data = super().clean()
        strength = cleaned_data.get('strength')
        dexterity = cleaned_data.get('dexterity')
        constitution = cleaned_data.get('constitution')
        intelligence = cleaned_data.get('intelligence')
        wisdom = cleaned_data.get('wisdom')
        charm = cleaned_data.get('charm')
        for score in [strength, dexterity, constitution, intelligence, wisdom, charm]:
            if score < 1 | score > 20:
                raise forms.ValidationError('One or more attributes entered are not within 1 and 20.')


class PointCharacterAttributesForm:
    strength = forms.IntegerField(widget=forms.NumberInput())
    dexterity = forms.IntegerField(widget=forms.NumberInput())
    constitution = forms.IntegerField(widget=forms.NumberInput())
    intelligence = forms.IntegerField(widget=forms.NumberInput())
    wisdom = forms.IntegerField(widget=forms.NumberInput())
    charm = forms.IntegerField(widget=forms.NumberInput())

    class Meta:
        model = Character
        fields = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charm']

    def clean(self):
        pointsSpent = 0
        cleaned_data = super().clean()
        strength = cleaned_data.get('strength')
        dexterity = cleaned_data.get('dexterity')
        constitution = cleaned_data.get('constitution')
        intelligence = cleaned_data.get('intelligence')
        wisdom = cleaned_data.get('wisdom')
        charm = cleaned_data.get('charm')
        for score in [strength, dexterity, constitution, intelligence, wisdom, charm]:
            if score <= 13:
                pointsSpent += score - 8
            else:
                pointsSpent += 5 + 2 * (score - 13)
        if not pointsSpent == 27:
            raise forms.ValidationError(f'The attribute scores you have chosen cost {pointsSpent} points, which is not '
                                        '27.')


class StandardCharacterAttributesForm:
    strength = forms.IntegerField(widget=forms.NumberInput())
    dexterity = forms.IntegerField(widget=forms.NumberInput())
    constitution = forms.IntegerField(widget=forms.NumberInput())
    intelligence = forms.IntegerField(widget=forms.NumberInput())
    wisdom = forms.IntegerField(widget=forms.NumberInput())
    charm = forms.IntegerField(widget=forms.NumberInput())

    class Meta:
        model = Character
        fields = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charm']

    def clean(self):
        flags = 6*[False]
        # Contains whether a value in the standard attribute array ([8, 10, 12, 13, 14, 15]) has been used
        cleaned_data = super().clean()
        strength = cleaned_data.get('strength')
        dexterity = cleaned_data.get('dexterity')
        constitution = cleaned_data.get('constitution')
        intelligence = cleaned_data.get('intelligence')
        wisdom = cleaned_data.get('wisdom')
        charm = cleaned_data.get('charm')
        for score in [strength, dexterity, constitution, intelligence, wisdom, charm]:
            if score == 8:
                if flags[0]:
                    raise forms.ValidationError(f'The attribute score {score} is used more than once, please use the '
                                                f'values (8, 10, 12, 13, 14, 15) once each.')
                flags[0] = True
            if score == 10:
                if flags[1]:
                    raise forms.ValidationError(f'The attribute score {score} is used more than once, please use the '
                                                f'values (8, 10, 12, 13, 14, 15) once each.')
                flags[1] = True
            if score == 12:
                if flags[2]:
                    raise forms.ValidationError(f'The attribute score {score} is used more than once, please use the '
                                                f'values (8, 10, 12, 13, 14, 15) once each.')
                flags[2] = True
            if score == 13:
                if flags[3]:
                    raise forms.ValidationError(f'The attribute score {score} is used more than once, please use the '
                                                f'values (8, 10, 12, 13, 14, 15) once each.')
                flags[3] = True
            if score == 14:
                if flags[4]:
                    raise forms.ValidationError(f'The attribute score {score} is used more than once, please use the '
                                                f'values (8, 10, 12, 13, 14, 15) once each.')
                flags[4] = True
            if score == 15:
                if flags[5]:
                    raise forms.ValidationError(f'The attribute score {score} is used more than once, please use the '
                                                f'values (8, 10, 12, 13, 14, 15) once each.')
                flags[5] = True
        for flag in flags:
            if not flag:
                raise forms.ValidationError(f'The attribute score {score} is used more than once, please use the '
                                            f'values (8, 10, 12, 13, 14, 15) once each.')
