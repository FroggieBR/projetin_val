from rest_framework import serializers
from .models import Player, Team, Tournament

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class TournamentSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Tournament
        fields = '__all__'