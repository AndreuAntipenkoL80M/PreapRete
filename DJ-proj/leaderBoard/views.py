from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import PlayerScores
from .forms import getPlayerName
import json


def index(request):
    return render(request, 'leaderBoard/Jobing.html')
#def addition(request):
#    return render()

def ajax_get_player_scores(request):
    scores = PlayerScores.objects.all().values('name', 'score')
    scores = list(scores)
    dict_scores={}
    for i in range(len(scores)):
        dict_scores[i] = scores[i]
    return JsonResponse(dict_scores)

def ajax_post_player_scores(request):
    pass
    new_score_record = json.load(request)
    print(new_score_record)
    new_rec = PlayerScores.objects.create(name = new_score_record['name'], score = new_score_record['score'])
    new_rec.save()
    scores = PlayerScores.objects.all().values('name', 'score')
    scores = list(scores)
    dict_scores={}
    for i in range(len(scores)):
        dict_scores[i] = scores[i]
    return JsonResponse(dict_scores)

def request_form(request):
    return render(request, "leaderBoard/formImporter.html", {"form": getPlayerName})
