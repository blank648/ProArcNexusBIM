from django.urls import path
from .views import (
    SetareListView, SetareCreateView,
    SetareUpdateView, SetareDeleteView
)

app_name = 'settings_app'

urlpatterns = [
    path('', SetareListView.as_view(), name='list'),
    path('create/', SetareCreateView.as_view(), name='create'),
    path('edit/<int:pk>/',   SetareUpdateView.as_view(), name='edit'),
    path('sterge/<int:pk>/', SetareDeleteView.as_view(), name='delete'),
]