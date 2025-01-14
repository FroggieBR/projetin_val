# Generated by Django 5.1.3 on 2024-11-10 04:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id_nick', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('nick', models.CharField(max_length=50, unique=True)),
                ('role', models.CharField(choices=[('SENTINEL', 'Sentinel'), ('DUELIST', 'Duelist'), ('CONTROLLER', 'Controller'), ('INITIATOR', 'Initiator'), ('FLEX', 'Flex')], max_length=50)),
                ('mapa', models.CharField(choices=[('ASCENT', 'Ascent'), ('BIND', 'Bind'), ('BREEZE', 'Breeze'), ('FRACTURE', 'Fracture'), ('HAVEN', 'Haven'), ('ICEBOX', 'Icebox'), ('LOTUS', 'Lotus'), ('PEARL', 'Pearl'), ('SPLIT', 'Split')], max_length=50)),
                ('agent', models.CharField(max_length=100)),
                ('rounds', models.IntegerField()),
                ('rating', models.FloatField()),
                ('kast', models.DecimalField(decimal_places=2, max_digits=5)),
                ('adr', models.FloatField()),
                ('acs', models.FloatField()),
                ('hs', models.DecimalField(decimal_places=2, max_digits=5)),
                ('kills', models.IntegerField()),
                ('deaths', models.IntegerField()),
                ('assists', models.IntegerField()),
                ('fk', models.IntegerField()),
                ('fd', models.IntegerField()),
                ('cl', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cl_win', models.IntegerField()),
                ('cl_played', models.IntegerField()),
                ('kmax', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Player',
                'verbose_name_plural': 'Players',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id_team', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('time', models.CharField(max_length=100, unique=True)),
                ('region', models.CharField(max_length=100)),
                ('coach', models.CharField(max_length=100)),
                ('jogador', models.ManyToManyField(related_name='teams', to='valorant_app.player')),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
            },
        ),
        migrations.AddField(
            model_name='player',
            name='time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='valorant_app.team'),
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id_tournament', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('tournament', models.CharField(max_length=100, unique=True)),
                ('time', models.ManyToManyField(related_name='tournaments', to='valorant_app.team')),
            ],
            options={
                'verbose_name': 'Tournament',
                'verbose_name_plural': 'Tournaments',
            },
        ),
        migrations.AddField(
            model_name='player',
            name='camp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='valorant_app.tournament'),
        ),
    ]
