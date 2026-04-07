from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('ajax_get_player_scores', views.ajax_get_player_scores),
    path('ajax_post_player_scores', views.ajax_post_player_scores),
    path('request_form', views.request_form)
]