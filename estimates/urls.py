from django.urls import path
from .views import (
    DevizListView, DevizCreateView, DevizUpdateView,
    DevizDeleteView, DevizPDFView
)

app_name='estimates'

urlpatterns = [
    path('', DevizListView.as_view(), name='list'),
    path('adauga/', DevizCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', DevizUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', DevizDeleteView.as_view(), name='delete'),
    path('pdf/<int:pk>/', DevizPDFView.as_view(), name='pdf'),
]