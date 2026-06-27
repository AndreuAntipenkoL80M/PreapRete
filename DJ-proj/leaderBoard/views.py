from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import PlayerScores
from .forms import getPlayerName, registerUser, loginUser, updateUser, updatePassword
import json


def index(request):
    return render(request, 'leaderBoard/Jobing.html')
#def addition(request):
#    return render()

def ajax_get_player_scores(request):
    scores = PlayerScores.objects.all().values('name', 'score', 'username')
    scores = list(scores)
    dict_scores={}
    for i in range(len(scores)):
        dict_scores[i] = scores[i]
    return JsonResponse(dict_scores)

def ajax_post_player_scores(request):
    new_score_record = json.load(request)
    print(new_score_record)
    if request.user.is_authenticated:
        new_rec = PlayerScores.objects.create(name = request.user.first_name, score = new_score_record['score'], username = request.user.username, userkey  = request.user)
        new_rec.save()
        scores = PlayerScores.objects.all().values('name', 'score', "username")
        scores = list(scores)
        dict_scores={}
        for i in range(len(scores)):
            dict_scores[i] = scores[i]
        return JsonResponse(dict_scores)
    else:
        new_rec = PlayerScores.objects.create(name = new_score_record['name'], score = new_score_record['score'])
        new_rec.save()
        scores = PlayerScores.objects.all().values('name', 'score')
        scores = list(scores)
        dict_scores={}
        for i in range(len(scores)):
            dict_scores[i] = scores[i]
        return JsonResponse(dict_scores)


def send_game_instance(request):
    if request.user.is_authenticated:
        user = request.user.first_name
        response = JsonResponse({"user": user})
        response["user_is_auth"] = True
        return response
    else:
        response = render(request, "leaderBoard/formImporter.html", {"form": getPlayerName, "formid": "req_unindent_player", "form_header": "Сохранить запись",})
        response["user_is_auth"] = False
        return response



def profile_handler(request):

    if request.user.is_authenticated:
        response = render(request, "leaderBoard/authHandler.html", {"exist_user_to_auth": True})
        return response
    else:
        return render(request, "leaderBoard/authHandler.html", {"exist_user_to_auth": False})

def auth_handler(request):
    if request.method == "POST":
        print(request.POST)
        temp_form = loginUser(request.POST)
        if temp_form.is_valid():
            temp_form = temp_form.cleaned_data
            print(temp_form)
            username = temp_form["userName"]
            password = temp_form["passName"]
            user = authenticate(request, username = username, password = password)
            if user:
                login(request, user)
                answer = JsonResponse({"text": user.get_full_name()})
                answer['typeOfAction'] = "greet"
                return answer
            else:
                answer = JsonResponse({"text": ""})
                answer['typeOfAction'] = "wrongCredentials"
                return answer
    else: 
        response = render(request, "leaderBoard/formImporter.html", {"form": loginUser, "formid": "auth_user", "form_header": "Вход в учетную запись",
                                                             "formmethod": "method = POST"})
        response['back_address'] = "/auth_handler"
        return response
    


def reg_user(request):
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
                login(request, new_account)
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
        response = render(request, "leaderBoard/formImporter.html", {"form": registerUser, "formid": "reg_user", "form_header": "Создание учетной записи",
                                                              "formmethod": "method = POST"})
        response['back_address'] = "/reg_user"
        return response
    
def user_exit(request):
    logout(request)
    print(request.user)
    response = HttpResponse()
    response.headers["typeofaction"] = "goodbye"
    return response

def del_user(request):
    annihilatedUser = User.objects.filter(username=request.user)
    logout(request)
    annihilatedUser.delete()
    response = HttpResponse()
    response.headers["typeofaction"] = "farewell"
    return response

def upd_pass(request):
    if request.method == "POST":
        temp_form = updatePassword(request.POST)
        if temp_form.is_valid():
            temp_form = temp_form.cleaned_data
            print(temp_form, request.user)
            if temp_form["newPassword"] == temp_form["confirmNewPassword"]:
                request.user.set_password(temp_form["newPassword"])
                answer  = JsonResponse({"text": request.user.username})
                answer['typeOfAction'] = "newPasswordApplied"
                return answer
            else:
                answer  = JsonResponse({"text": request.user.username})
                answer['typeOfAction'] = "newPasswordRejected"
                return answer 
    else:
        response = render(request, "leaderBoard/formImporter.html", {"form": updatePassword, "formid": "upd_pass", "form_header": "Изменение пароля",
                                                              "formmethod": "method = POST"})
        response['back_address'] = "/upd_pass"
        return response


def upd_user(request):
    if request.method == "POST":
        temp_form = updateUser(request.POST)
        if temp_form.is_valid():
            temp_form = temp_form.cleaned_data
            request.user.first_name = temp_form["firstName"]
            request.user.last_name = temp_form["lastName"]   
            request.user.save()
            print(request.user.get_full_name())
            answer = JsonResponse({"text": request.user.get_full_name()})
            answer['typeOfAction'] = "updated"
            return answer
        else:
            print("abc")
            answer  = JsonResponse({"text": temp_form["userName"]})
            answer['typeOfAction'] = "updatedNot"
            return answer
    else:
        print(request.user.first_name)
        response = render(request, "leaderBoard/formImporter.html", {"form": updateUser(initial={"firstName" : request.user.first_name, "lastName" : request.user.last_name}), "formid": "upd_user", "form_header": "Изменение учетной записи",
                                                              "formmethod": "method = POST"})
        response['back_address'] = "/upd_user"
        return response
