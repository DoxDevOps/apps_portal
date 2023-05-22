from django.forms import ModelForm
from .models import App
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class AppForm(ModelForm):
    icon = forms.FileField()
    class Meta:
        model = App
        fields = ['name', 'description', 'url']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
