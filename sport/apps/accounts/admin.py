from django.contrib import admin
from sport.apps.accounts.models import User, Player, Trainer, Specialty
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


admin.site.register(User)
admin.site.register(Specialty)
admin.site.register(Player)
admin.site.register(Trainer)
