from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegistrationForm(UserCreationForm):

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Imię'}))

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Nazwisko'}))

    email = forms.EmailField(help_text='proszę wprowadzić prawidłowy email',
        widget=forms.EmailInput(
        attrs={'placeholder': 'Email'}))

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Hasło'}))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Powtórz hasło'}))

    class Meta:
        model = User
        fields = [
                  'first_name', 'last_name', 'email',
                  'password1', 'password2'
        ]
