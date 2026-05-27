from django import forms
from .models import PlayerScores
from django.contrib.auth.models import User


class getPlayerName(forms.Form):
    name = forms.CharField(max_length=PlayerScores._meta.get_field('name').max_length, label="Ваше имя:")

class registerUser(forms.Form):
    firstName = forms.CharField(max_length=User._meta.get_field('first_name').max_length, label="Ваше имя:", initial="xuy")
    lastName = forms.CharField(max_length=User._meta.get_field('last_name').max_length, label="Ваша фамилия:", initial="xuy")
    userName = forms.CharField(max_length=User._meta.get_field('first_name').max_length, label="Ваш login:", initial="xuy")
    passName = forms.CharField(max_length=User._meta.get_field('password').max_length, label="Пароль:", widget=forms.PasswordInput, initial="xuy")

class loginUser(forms.Form):
    pass