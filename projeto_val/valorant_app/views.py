from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Player, Team, Tournament
from .serializers import PlayerSerializer, TeamSerializer, TournamentSerializer

# Create your views here.

class PlayerViewSet(ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    
class TournamentViewSet(ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

    