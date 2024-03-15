from django.db import models


class Specialty(models.Model):

    name = models.CharField('Nome', max_length=100, unique=True)

    def __str__(self):
        return self.name
