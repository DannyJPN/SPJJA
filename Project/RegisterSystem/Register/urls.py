from django.urls import path
from . import views


urlpatterns = [
	path('ranking/', views.index,name="ranking"),
    path('matches/', views.matchlist,name="matchlist"),
    path('teams/', views.teamlist,name="teamlist"),
    
    
    path('players/<int:player_id>/', views.player_detail,name="player_detail"),
    path('teams/<int:team_id>/', views.team_detail,name="team_detail"),
    
    path('newplayer/', views.player_form, name ='player_form'),
    path('newteam/', views.team_form, name ='team_form'),
    path('newmatch/', views.match_form, name ='match_form'),
    
]
