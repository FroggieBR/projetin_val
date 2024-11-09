from django.contrib import admin
from .models import Player, Team, Tournament

# Register your models here.

@admin.site.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = (
                'nick',
                'team',
                'role',
                'camp',
                'mapa',
                'agent',
                'rounds',
                'rating',
                'kast',
                'adr',
                'acs',
                'hs'
                'kills',
                'deaths',
                'assists',
                'kda',
                'kpr',
                'apr',
                'dpr',
                'involvement_duels',
                'sucess_duels',
                'fk',
                'fd',
                'fk_part',
                'fk_sucess',
                'fkpr',
                'fdpr',
                'cl',
                'cl_win',
                'cl_played',
                'cl_part',
                'cl_sucess',
                'kmax'
            )
@admin.site.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = (
                'team',
                'country', 
                'region',
                'coach',  
                'players'
            )

@admin.site.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ('tournament',
                    'teams',)