from django.db import models
from sport.apps.accounts.models.user import User
from sport.apps.accounts.models.player_specialty import Specialty
from sport.apps.accounts.models.player import Player
from django.core.exceptions import ValidationError


class Trainer(models.Model):

    SEX_CHOICES = (
        ('M', 'MASCULINO'),
        ('F', 'FEMENINO')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    sex = models.CharField('Sexo', max_length=1, choices=SEX_CHOICES)
    year_exp = models.IntegerField('Anos de Experiencia')

    def clean(self):
        super().clean()
        if Player.objects.filter(user=self.user).exists():
            raise ValidationError("Usuário já fixado com Jogador.")

    def __str__(self):
        return self.user.get_full_name()
