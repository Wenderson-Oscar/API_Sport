from rest_framework import serializers
from sport.apps.accounts.models import User, Player, Trainer, Specialty


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'profile', 'phone', 'email', 'password']
        extra_kwargs = {
            'first_name': {'write_only': True, 'required': False},
            'last_name': {'write_only': True, 'required': False},
            'password': {'write_only': True, 'required': False},
            'email': {'write_only': True, 'required': False},
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class SpecialtySerializer(serializers.ModelSerializer):

    class Meta:
        model = Specialty
        fields = ['name']


class UserUpdateSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    specialty = serializers.PrimaryKeyRelatedField(
        queryset=Specialty.objects.all(), required=False, write_only=True)
    kg = serializers.FloatField(write_only=True, required=False)
    height = serializers.FloatField(write_only=True, required=False)

    class Meta:
        model = Player
        fields = ['user', 'specialty', 'kg', 'height', 'sex']

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})
        user_serializer = UserSerializer(
            instance.user, data=user_data, partial=True)
        if user_serializer.is_valid(raise_exception=True):
            user_serializer.save()

        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance


class PlayerSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    kg = serializers.FloatField(write_only=True, required=False)
    height = serializers.FloatField(write_only=True, required=False)
    sex = serializers.ChoiceField(
        choices=Player.SEX_CHOICES, write_only=True, required=False)

    class Meta:
        model = Player
        fields = ['user', 'specialty', 'kg', 'height', 'sex']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        specialty_data = validated_data.pop('specialty')
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        player, created = Player.objects.update_or_create(
            user=user, specialty=specialty_data, **validated_data)
        return player


class TrainerSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Trainer
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(
            UserSerializer(), validated_data=user_data)
        trainer, created = Trainer.objects.update_or_create(
            user=user, **validated_data
        )
        return trainer
