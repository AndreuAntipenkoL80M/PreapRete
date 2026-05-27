from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import PlayerScores
from .forms import getPlayerName, registerUser
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
    new_score_record = json.load(request)
    #print(new_score_record)
    new_rec = PlayerScores.objects.create(name = new_score_record['name'], score = new_score_record['score'])
    new_rec.save()
    scores = PlayerScores.objects.all().values('name', 'score')
    scores = list(scores)
    dict_scores={}
    for i in range(len(scores)):
        dict_scores[i] = scores[i]
    return JsonResponse(dict_scores)

def profile_handler(request):
    return req_user(request)

def send_game_instance(request):
    return render(request, "leaderBoard/formImporter.html", {"form": getPlayerName, "formid": "req_unindent_player", "form_header": "Сохранить запись",})

def req_user(request):
    if request.method == "POST":
        print(request.POST)
        temp_form = registerUser(request.POST)
        if temp_form.is_valid():
            temp_form = temp_form.cleaned_data    
            if not User.objects.filter(username=temp_form['userName']).exists():
                new_account = User.objects.create_user(username = temp_form["userName"], first_name = temp_form["firstName"],
                                    last_name = temp_form["lastName"])
                new_account.set_password(temp_form['passName'])
                new_account.save()
                print(new_account.get_full_name())
                answer = JsonResponse({"text": new_account.get_full_name()})
                answer['typeOfAction'] = "welcome"
                return answer
            else:
                print("abc")
                answer  = JsonResponse({"text": temp_form["userName"]})
                answer['typeOfAction'] = "login_occupied"
                return answer
    else:
        return render(request, "leaderBoard/formImporter.html", {"form": registerUser, "formid": "req_user", "form_header": "Создание учетной записи",
                                                             "formaction": "action = /req_user", "formmethod": "method = POST"})
