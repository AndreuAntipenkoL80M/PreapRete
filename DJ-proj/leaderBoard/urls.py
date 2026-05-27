from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('ajax_get_player_scores', views.ajax_get_player_scores),
    path('ajax_post_player_scores', views.ajax_post_player_scores),
    path('send_game_instance', views.send_game_instance),
    path('req_user', views.req_user),
    path('profile_handler', views.profile_handler),
]