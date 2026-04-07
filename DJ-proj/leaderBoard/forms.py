from django import forms
from .models import PlayerScores


class getPlayerName(forms.Form):
    name = forms.CharField(max_length=PlayerScores._meta.get_field('name').max_length, label="Ваше имя:")