from django.urls import path
from .views import ReportSummaryView, ReportPDFView

app_name = 'reports'

urlpatterns = [
    path('', ReportSummaryView.as_view(), name='report-summary'),
    path('pdf/', ReportPDFView.as_view(), name='report-pdf'),
]