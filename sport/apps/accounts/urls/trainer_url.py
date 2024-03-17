from django.urls import path
from sport.apps.accounts.viewsets.trainer import (
    ListTrainerViewSet, CreateTrainerViewSet, DeleteTrainerViewSet, UpdateTrainerViewSet)

urlpatterns = [
    path('trainers/', ListTrainerViewSet.as_view({'get': 'list'})),
    path('create/trainer/', CreateTrainerViewSet.as_view({'post': 'create'})),
    path('delete/trainer/<int:pk>/',
         DeleteTrainerViewSet.as_view({'delete': 'destroy'})),
    path('update/trainer/<int:pk>/',
         UpdateTrainerViewSet.as_view({'put': 'update'})),
]
