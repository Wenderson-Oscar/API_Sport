from rest_framework import serializers
from sport.apps.team.models import Team
from sport.apps.accounts.serializers import PlayerSerializer, TrainerSerializer, Player, Trainer
from django.core.exceptions import ValidationError


class CreateTeamSerializer(serializers.ModelSerializer):

    players = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Player.objects.all())
    trainers = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Trainer.objects.all())

    class Meta:
        model = Team
        fields = '__all__'
        extra_kwargs = {
            'players': {'write_only': True, 'required': False},
            'trainers': {'write_only': True, 'required': False},
            'name': {'write_only': True, 'required': False},
            'players_limit': {'write_only': True, 'required': False},
            'trainers_limit': {'write_only': True, 'required': False}
        }

    def validate(self, data):
        player_limit = data.get(
            'players_limit', self.instance.players_limit if self.instance else None)
        trainer_limit = data.get(
            'trainers_limit', self.instance.trainers_limit if self.instance else None)
        current_players = self.instance.players.all() if self.instance else []
        current_trainers = self.instance.trainers.all() if self.instance else []
        proposed_players = data.get('players', current_players)
        proposed_trainers = data.get('trainers', current_trainers)
        total_players = len(set(proposed_players) | set(current_players))
        total_trainers = len(set(proposed_trainers) | set(current_trainers))
        if player_limit is not None and total_players > player_limit:
            raise ValidationError(
                {'players': f'A quantidade de jogadores excede o limite permitido: ({player_limit}).'})
        if trainer_limit is not None and total_trainers > trainer_limit:
            raise ValidationError(
                {'trainers': f'A quantidade de treinadores excede o limite permitido: ({trainer_limit}).'})
        return data

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr not in ['players', 'trainers']:
                setattr(instance, attr, value)
        instance.save()
        if 'players' in self.initial_data:
            players = validated_data.get('players')
            instance.players.set(players)
        if 'trainers' in self.initial_data:
            trainers = validated_data.get('trainers')
            instance.trainers.set(trainers)
        return instance


class TeamSerializer(serializers.ModelSerializer):

    players = PlayerSerializer(many=True)
    trainers = TrainerSerializer(many=True)

    class Meta:
        model = Team
        fields = '__all__'
