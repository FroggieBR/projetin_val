from django.db import models

class Player(models.Model):
    class Role(models.TextChoices):
        SENTINEL = 'SENTINEL'
        DUELIST = 'DUELIST'
        CONTROLLER = 'CONTROLLER'
        INITIATOR = 'INITIATOR'
        FLEX = 'FLEX'
    
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
    time = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='players')
    role = models.CharField(max_length=50, choices=Role.choices)
    camp = models.ForeignKey('Tournament', on_delete=models.CASCADE, related_name='players')
    mapa = models.CharField(max_length=50, choices=Map.choices)
    agent = models.CharField(max_length=100)
    rounds = models.IntegerField()
    rating = models.FloatField()
    kast = models.DecimalField(max_digits=5, decimal_places=2)
    adr = models.FloatField()
    acs = models.FloatField()
    hs = models.DecimalField(max_digits=5, decimal_places=2)
    kills = models.IntegerField()
    deaths = models.IntegerField()
    assists = models.IntegerField()
    fk = models.IntegerField()
    fd = models.IntegerField()
    cl = models.DecimalField(max_digits=5, decimal_places=2)
    cl_win = models.IntegerField()
    cl_played = models.IntegerField()
    kmax = models.IntegerField()

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'

    def __str__(self):
        return self.nick

    @property
    def kda(self):
        return (self.kills + self.assists) / self.deaths if self.deaths != 0 else self.kills + self.assists

    @property
    def kpr(self):
        return self.kills / self.rounds if self.rounds != 0 else 0

    @property
    def apr(self):
        return self.assists / self.rounds if self.rounds != 0 else 0

    @property
    def dpr(self):
        return self.deaths / self.rounds if self.rounds != 0 else 0

    @property
    def duels_part(self):
        return (self.kills + self.deaths) / self.rounds if self.rounds != 0 else 0

    @property
    def sucess_duels(self):
        return self.kills / (self.kills + self.deaths) if (self.kills + self.deaths) != 0 else 0

    @property
    def fk_part(self):
        return (self.fk + self.fd) / self.rounds if self.rounds != 0 else 0

    @property
    def fk_sucess(self):
        return self.fk / (self.fk + self.fd) if (self.fk + self.fd) != 0 else 0

    @property
    def fkpr(self):
        return self.fk / self.rounds if self.rounds != 0 else 0

    @property
    def fdpr(self):
        return self.fd / self.rounds if self.rounds != 0 else 0

    @property
    def cl_part(self):
        return (self.cl_win + self.cl_played) / self.rounds if self.rounds != 0 else 0

    @property
    def cl_sucess(self):
        return self.cl_win / (self.cl_win + self.cl_played) if (self.cl_win + self.cl_played) != 0 else 0


class Team(models.Model):
    id_team = models.IntegerField(primary_key=True, unique=True, auto_created=True)
    time = models.CharField(max_length=100, unique=True)
    region = models.CharField(max_length=100)
    coach = models.CharField(max_length=100)
    jogador = models.ManyToManyField(Player, related_name='teams')

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'
    
    def __str__(self):
        return self.team

class Tournament(models.Model):
    id_tournament = models.IntegerField(primary_key=True, unique=True, auto_created=True)
    tournament = models.CharField(max_length=100, unique=True)
    time = models.ManyToManyField(Team, related_name='tournaments')

    class Meta:
        verbose_name = 'Tournament'
        verbose_name_plural = 'Tournaments'
    
    def __str__(self):
        return self.tournament
