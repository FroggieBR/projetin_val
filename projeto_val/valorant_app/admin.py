from django.contrib import admin
from .models import Player, Team, Tournament

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('nick', 'time', 'role', 'mapa', 'agent', 'rating', 'kast', 'adr', 'acs', 'hs', 'kills', 'deaths', 'assists', 'kda', 'kpr', 'apr', 'dpr', 'duels_part', 'sucess_duels', 'fk_part', 'fk_sucess', 'fkpr', 'fdpr', 'cl_part', 'cl_sucess')
    list_filter = ('nick', 'agent', 'time', 'role', 'mapa')
    search_fields = ('nick', 'agent')
    readonly_fields = ('kda', 'kpr', 'apr', 'dpr', 'duels_part', 'sucess_duels', 'fk_part', 'fk_sucess', 'fkpr', 'fdpr', 'cl_part', 'cl_sucess')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('time', 'region', 'coach')
    search_fields = ('time', 'region', 'coach')
    filter_horizontal = ('jogador',)  # Para permitir selecionar vários jogadores no admin

@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ('tournament',)
    search_fields = ('tournament',)
    filter_horizontal = ('time',)  # Para permitir selecionar vários times no admin