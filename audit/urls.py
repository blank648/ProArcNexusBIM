from django.urls import path
from .views import AuditLogView

app_name = 'audit'

urlpatterns = [
    path('logs/', AuditLogView.as_view(), name='logs'),
]