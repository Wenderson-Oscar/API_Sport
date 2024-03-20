from django.shortcuts import render
from rest_framework import mixins, viewsets
from sport.apps.team.models import Team
from sport.apps.team.serializers import TeamSerializer, CreateTeamSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser


class TeamViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):

    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class CreateTeamViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Team.objects.all()
    serializer_class = CreateTeamSerializer


class DeleteTeamViewSet(mixins.DestroyModelMixin, viewsets.GenericViewSet):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get_object(self):
        obj = self.get_queryset().first()
        self.check_object_permissions(self.request, obj)
        return obj


class UpdateTeamViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Team.objects.all()
    serializer_class = CreateTeamSerializer
