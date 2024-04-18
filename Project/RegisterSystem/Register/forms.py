from django import forms
from .models import Player,Team        ,Match

class PlayerForm (forms.ModelForm):
    class Meta:
        model = Player
        fields = [
            'birthdate',
            'name',
            'surname',
            'team',
            
        ]
class TeamForm (forms.ModelForm):
    class Meta:
        model = Team
        fields = [
            'name',
            'league',
            
        ]
class MatchForm (forms.ModelForm):
    class Meta:
        model = Match
        fields = [
            'player1',
            'player2',
            'set1',
            'set2',
            'set3',
            'set4',
            'set5',
            'date_of_occ',
            
        ]
