from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField


class CreateAccountForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        # field_classes = {'username': UsernameField}
        layout = [
            ("Field", "username"),
            ("Field", "password1"),
            ("Field", "password2")
        ]

    def __init__(self, *args, **kwargs):
        super(__class__, self).__init__(*args, **kwargs)

        placeholders = {
            "username": "Username",
            "password1": "Password",
            "password2": "Verify Password"
        }

        for key, value in placeholders.items():
            self.fields[key].widget.attrs["placeholder"] = value


class LoginForm(AuthenticationForm):
    class Meta:
        fields = ["username", "password"]
        layout = [
            ("Field", "username"),
            ("Field", "password")
        ]

    def __init__(self, *args, **kwargs):
        super(__class__, self).__init__(*args, **kwargs)

        placeholders = {
            "username": "Username",
            "password": "Password",
        }

        for key, value in placeholders.items():
            self.fields[key].widget.attrs["placeholder"] = value
