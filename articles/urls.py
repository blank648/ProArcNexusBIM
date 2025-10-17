from django.urls import path
from .views import (
    ArticolListView, ArticolCreateView,
    ArticolUpdateView, ArticolDeleteView
)

app_name = 'articles'

urlpatterns = [
    path('',                 ArticolListView.as_view(),   name='list'),
    path('adauga/',          ArticolCreateView.as_view(), name='create'),
    path('<int:pk>/edit/',   ArticolUpdateView.as_view(), name='edit'),
    path('<int:pk>/sterge/', ArticolDeleteView.as_view(), name='delete'),
]