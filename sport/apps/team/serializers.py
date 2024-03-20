from rest_framework import serializers
from sport.apps.team.models import Team
from sport.apps.accounts.serializers import PlayerSerializer, TrainerSerializer, Player, Trainer


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
