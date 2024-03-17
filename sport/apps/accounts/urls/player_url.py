from django.urls import path
from sport.apps.accounts.viewsets.player import (
    ListPlayerViewSet, CreatePlayerViewSet, UpdatePlayerView, DeletePLayerView)

urlpatterns = [
    path('players/', ListPlayerViewSet.as_view({'get': 'list'})),
    path('players/create/',
         CreatePlayerViewSet.as_view({'post': 'create'})),
    path('players/update/<int:pk>/',
         UpdatePlayerView.as_view({'put': 'update'})),
    path('players/delete/<int:pk>/',
         DeletePLayerView.as_view({'delete': 'destroy'})),
]
