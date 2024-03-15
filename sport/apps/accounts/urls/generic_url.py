from django.urls import path
from sport.apps.accounts.viewsets.generic import *

urlpatterns = [
    path('login/', LoginViewSet.as_view({'get': 'list'}), name='login'),
    path('logout/', LogoutViewSet.as_view({'get': 'list'}), name='logout'),
]
