from django.urls import path
from sport.apps.team.views import TeamViewSet, CreateTeamViewSet, DeleteTeamViewSet, UpdateTeamViewSet


urlpatterns = [
    path('teams/', TeamViewSet.as_view({'get': 'list'})),
    path('create/team/', CreateTeamViewSet.as_view({'post': 'create'})),
    path('delete/team/<int:pk>/',
         DeleteTeamViewSet.as_view({'delete': 'destroy'})),
    path('update/team/<int:pk>/',
         UpdateTeamViewSet.as_view({'put': 'update'})),
]
