from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from datetime import timezone


class UserManager(UserManager):

    def create_user(self, email: str, password=None, **extra_fields):
        if not email:
            raise ValueError("Email é Obrigatorio!")
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email: str, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('first_name', 'User')
        extra_fields.setdefault('last_name', 'Admin')
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):

    username = None
    profile = models.ImageField(
        'Foto de Perfil', blank=True, null=True, upload_to='media/profile/',
        default='profile/not_img.jpg')
    email = models.EmailField('Email', max_length=150, unique=True,
                              error_messages={'unique': 'Email já Cadastrado!'})
    phone = models.IntegerField(
        'Número de Telefone', unique=True, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField('Primeiro Nome', max_length=150)
    last_name = models.CharField('Ultimo Nome', max_length=150)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.get_full_name()
