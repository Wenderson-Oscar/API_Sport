from django.db import models
from sport.apps.accounts.models.user import User
from sport.apps.accounts.models.player_specialty import Specialty


class Player(models.Model):

    SEX_CHOICES = (
        ('M', 'MASCULINO'),
        ('F', 'FEMENINO')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    kg = models.FloatField('KG', blank=True, null=True)
    height = models.FloatField('Altura', blank=True, null=True)
    sex = models.CharField('Sexo', max_length=1, choices=SEX_CHOICES)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_full_name()
