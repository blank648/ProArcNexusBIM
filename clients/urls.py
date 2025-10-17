from django.urls import path
from .views import (
    ClientListView, ClientCreateView,
    ClientUpdateView, ClientDeleteView
)

app_name = 'clients'

urlpatterns = [
    path('', ClientListView.as_view(), name='list'),
    path('adauga/', ClientCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', ClientUpdateView.as_view(), name='edit'),
    path('<int:pk>/sterge/', ClientDeleteView.as_view(), name='delete'),

]