from rest_framework import viewsets, mixins
from sport.apps.accounts.models import User, Player
from sport.apps.accounts.serializers.serializer import PlayerSerializer, UserSerializer, UserUpdateSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class ListPlayerViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = PlayerSerializer
    queryset = Player.objects.all()


class CreatePlayerViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class UpdatePlayerView(mixins.UpdateModelMixin, viewsets.GenericViewSet):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserUpdateSerializer

    def get_queryset(self):
        return Player.objects.filter(user=self.request.user)

    def get_object(self):
        obj = self.get_queryset().first()
        self.check_object_permissions(self.request, obj)
        return obj


class DeletePLayerView(mixins.DestroyModelMixin, viewsets.GenericViewSet):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    def get_object(self):
        obj = self.get_queryset().first()
        self.check_object_permissions(self.request, obj)
        return obj
