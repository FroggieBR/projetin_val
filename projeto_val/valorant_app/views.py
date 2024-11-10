from django.shortcuts import render
from .models import Player, Team, Tournament
from .serializers import PlayerSerializer, TeamSerializer, TournamentSerializer
from rest_framework import viewsets

# Create your views here.

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class TeamViewSet(viewsets.ModelViewSet):    
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer