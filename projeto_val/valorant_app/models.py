from django.db import models

# Create your models here.

class Player(models.Model):
    class Role(models.TextChoices):
        SENTINEL = 'SENTINEL'
        DUELIST = 'DUELIST'
        CONTROLLER = 'CONTROLLER'
        INITIATOR = 'INITIATOR'
    
    class Map(models.TextChoices):
        ASCENT = 'ASCENT'
        BIND = 'BIND'
        BREEZE = 'BREEZE'
        FRACTURE = 'FRACTURE'
        HAVEN = 'HAVEN'
        ICEBOX = 'ICEBOX'
        LOTUS = 'LOTUS'
        PEARL = 'PEARL'
        SPLIT = 'SPLIT'
        
    id_nick = models.IntegerField(primary_key=True, unique=True, auto_created=True)
    nick = models.CharField(max_length=50, unique=True)
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=Role.choices)
    camp = models.ForeignKey('Tournament', on_delete=models.CASCADE)
    mapa = models.CharField(max_length=50, choices=Map.choices)
    agent = models.CharField(max_length=100)
    rounds = models.IntegerField()
    rating = models.FloatField()
    kast = models.DecimalField()
    adr = models.FloatField()
    acs = models.FloatField()
    hs = models.DecimalField()
    kills = models.IntegerField()
    deaths = models.IntegerField()
    assists = models.IntegerField()
    kda = ((kills + assists) / deaths) if deaths != 0 else (kills + assists)
    kpr = kills / rounds
    apr = assists / rounds
    dpr = deaths / rounds
    involvement_duels = (kills + deaths) / rounds
    sucess_duels = kills / (kills + deaths)
    fk = models.IntegerField()
    fd = models.IntegerField()
    fk_part = (fk + fd) / rounds
    fk_sucess = fk / (fk + fd)
    fkpr = fk / rounds
    fdpr = fd / rounds
    cl = models.DecimalField()
    cl_win = models.IntegerField()
    cl_played = models.IntegerField()
    cl_part = (cl_win + cl_played) / rounds
    cl_sucess = cl_win / (cl_win + cl_played)
    kmax = models.IntegerField()
    
    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'
    
    def __str__(self):
        return self.nick
    
class Team(models.Model):
    id_team = models.IntegerField(primary_key=True, unique=True, auto_created=True)
    team = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    coach = models.CharField(max_length=100, null=True, blank=True)
    player = models.ManyToManyField(Player)
    
    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'
    
    
    def __str__(self):
        return self.name
    
class Tournament(models.Model):
    id_tournament = models.IntegerField(primary_key=True, unique=True, auto_created=True)
    tournament = models.CharField(max_length=100, unique=True)
    team = models.ManyToManyField(Team)
    
    class Meta:
        verbose_name = 'Tournament'
        verbose_name_plural = 'Tournaments'

    
    def __str__(self):
        return self.name