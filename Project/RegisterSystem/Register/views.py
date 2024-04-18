from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from Register.models import Player,Match,Team
from .forms import PlayerForm,TeamForm,MatchForm
# Create your views here.

def index(request):
    players = Player.objects.all()
    matches = Match.objects.all()
    for match in matches:
        sets = (match.set1,match.set2,match.set3,match.set4,match.set5)
        for one in sets:
            if one is None:
                pass
            elif  int(one) >0:
                match.result1+=1
            else:
                match.result2+=1
    
    for player in players:
        for match in matches:
        
            if(match.player1.id is player.id and match.result1 is 3) or (match.player2.id is player.id and match.result2 is 3):
                player.wins = player.wins+1
                
            elif(match.player1.id is player.id and match.result2 is 3) or (match.player2.id is player and match.result1 is 3):
                player.loses = player.loses+1
        if player.wins+player.loses is not 0:
            player.bilance = 100* player.wins/ (player.wins+player.loses)        
    return render(request,'Register/index.html',{'players':players})

    
    
def player_detail(request,player_id):
    player = get_object_or_404(Player,pk=player_id)
    matches = Match.objects.all()
    fil_matches = []
    for match in matches:
        sets = (match.set1,match.set2,match.set3,match.set4,match.set5)
        for one in sets:
            if one is None:
                pass
            elif  int(one) >0:
                match.result1+=1
            else:
                match.result2+=1
    
    
    
    for match in matches:
        if match.player1.id is player.id or match.player2.id is player.id:
            fil_matches.append(match)
    for filmatch in fil_matches:
        if filmatch.player2.id is player.id:
            filmatch.player1,filmatch.player2 = filmatch.player2,filmatch.player1
            filmatch.result1,filmatch.result2 = filmatch.result2,filmatch.result1
            if filmatch.set1 is not None:
                filmatch.set1 = (-1) * int(filmatch.set1)
            if filmatch.set2 is not None:
                filmatch.set2 = (-1) * int(filmatch.set2)
            if filmatch.set3 is not None:
                filmatch.set3 = (-1) * int(filmatch.set3)
            if filmatch.set4 is not None:
                filmatch.set4 = (-1)  * int(filmatch.set4)
            if filmatch.set5 is not None:
                filmatch.set5 = (-1)  * int(filmatch.set5)
           
           
           
        if filmatch.set1 is  None:
            filmatch.set1 = " "
        if filmatch.set2 is  None:
            filmatch.set2 = " "
        if filmatch.set3 is  None:
            filmatch.set3 = " "
        if filmatch.set4 is  None:
            filmatch.set4 = " "
        if filmatch.set5 is  None:
            filmatch.set5 = " "
                
           
            
    return render(request, 'Register/player_detail.html',{"player":player,'fil_matches':fil_matches})   

def team_detail(request,team_id):
    team = get_object_or_404(Team,pk=team_id)
    team.playerlist=[]
    players = Player.objects.all()
    
    for player in players:
        if(player.team.id is team.id):
            team.playerlist.append(player)
    return render(request, 'Register/team_detail.html',{"team":team})   
    
    
def matchlist(request):
    matches = Match.objects.all()
    for match in matches:
        sets = (match.set1,match.set2,match.set3,match.set4,match.set5)
        for one in sets:
            if one is None:
                pass
            elif  int(one) >0:
                match.result1+=1
            else:
                match.result2+=1
        if match.set1 is  None:
            match.set1 = " "
        if match.set2 is  None:
            match.set2 = " "
        if match.set3 is  None:
            match.set3 = " "
        if match.set4 is  None:
            match.set4 = " "
        if match.set5 is  None:
            match.set5 = " "
                        
                
                
                
    return render(request,'Register/matchlist.html',{'matches':matches})
    
def teamlist(request):
    teams = Team.objects.all()
    return render(request,'Register/teamlist.html',{'teams':teams})
    
    
def player_form(request):
    form = PlayerForm(request.POST or None)
    if (form.is_valid()):
        form.save()    
    else:
        print("Form did not save")
    return render(request, 'Register/player_form.html',{"form":form})   

def team_form(request):
    form = TeamForm(request.POST or None)
    if (form.is_valid()):
        form.save()    
    else:
        print("Form did not save")
    return render(request, 'Register/team_form.html',{"form":form})   
    
def match_form(request):
    form = MatchForm(request.POST or None)
    
    if (form.is_valid()):
        form.save()    
    else:
        print("Form did not save")
    return render(request, 'Register/match_form.html',{"form":form})   
    
    

    

                                                                                 