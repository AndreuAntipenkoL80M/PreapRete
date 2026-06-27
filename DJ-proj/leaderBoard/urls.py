from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('ajax_get_player_scores', views.ajax_get_player_scores),
    path('ajax_post_player_scores', views.ajax_post_player_scores),
    path('send_game_instance', views.send_game_instance),
    path('reg_user', views.reg_user),
    path('profile_handler', views.profile_handler),
    path('auth_handler', views.auth_handler),
    path('user_exit', views.user_exit),
    path('del_user', views.del_user),
    path('upd_user', views.upd_user),
    path('upd_pass', views.upd_pass),   
]