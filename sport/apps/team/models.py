from django.db import models
from sport.apps.accounts.models import Player, Trainer


class Team(models.Model):

    name = models.CharField("Nome do time", max_length=50, unique=True)
    players_limit = models.IntegerField("Quantidade maxima de Jogadores")
    trainers_limit = models.IntegerField("Quantidade maxima de Treinadores")
    players = models.ManyToManyField(Player)
    trainers = models.ManyToManyField(Trainer)

    def __str__(self):
        return self.name
