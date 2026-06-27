from django import forms
from .models import PlayerScores
from django.contrib.auth.models import User


class getPlayerName(forms.Form):
    name = forms.CharField(max_length=PlayerScores._meta.get_field('name').max_length, label="Ваше имя:")

class registerUser(forms.Form):
    firstName = forms.CharField(max_length=User._meta.get_field('first_name').max_length, label="Ваше имя:", initial="xuy")
    lastName = forms.CharField(max_length=User._meta.get_field('last_name').max_length, label="Ваша фамилия:", initial="xuy")
    userName = forms.CharField(max_length=User._meta.get_field('username').max_length, label="Ваш login:", initial="xuy100")
    passName = forms.CharField(max_length=User._meta.get_field('password').max_length, label="Пароль:", widget=forms.PasswordInput)

class updateUser(forms.Form):
    firstName = forms.CharField(max_length=User._meta.get_field('first_name').max_length, label="Ваше имя:")
    lastName = forms.CharField(max_length=User._meta.get_field('last_name').max_length, label="Ваша фамилия:")

class loginUser(forms.Form):
    userName = forms.CharField(max_length=User._meta.get_field('username').max_length, label="Ваш login:", initial="xuy1000")
    passName = forms.CharField(max_length=User._meta.get_field('password').max_length, label="Пароль:", widget=forms.PasswordInput)

class updatePassword(forms.Form):
    newPassword = forms.CharField(max_length=User._meta.get_field('password').max_length, label="Пароль:", widget=forms.PasswordInput)
    confirmNewPassword = forms.CharField(max_length=User._meta.get_field('password').max_length, label="Пароль (x2):", widget=forms.PasswordInput)