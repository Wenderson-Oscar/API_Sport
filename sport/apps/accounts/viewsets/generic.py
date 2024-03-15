from rest_framework import viewsets, status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import logout


class LoginViewSet(viewsets.ViewSet):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, format=None):
        content = {
            'user': str(request.user),
        }
        return Response(content)


class LogoutViewSet(viewsets.ViewSet):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, format=None):
        logout(request)
        return Response(status=status.HTTP_200_OK)
