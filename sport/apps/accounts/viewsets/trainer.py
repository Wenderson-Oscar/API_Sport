from rest_framework import viewsets, mixins
from sport.apps.accounts.models import Trainer, User
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from sport.apps.accounts.serializers import TrainerSerializer, UserSerializer, UserUpdateSerializer


class ListTrainerViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer


class CreateTrainerViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer


class DeleteTrainerViewSet(mixins.DestroyModelMixin, viewsets.GenericViewSet):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    def get_object(self):
        obj = self.get_queryset().first()
        self.check_object_permissions(self.request, obj)
        return obj


class UpdateTrainerViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserUpdateSerializer

    def get_queryset(self):
        return Trainer.objects.filter(user=self.request.user)

    def get_object(self):
        obj = self.get_queryset().first()
        self.check_object_permissions(self.request, obj)
        return obj
