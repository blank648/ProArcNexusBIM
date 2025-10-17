from django import forms
from clients.models import Client

class ReportFilterForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    client = forms.ModelChoiceField(
        queryset=Client.objects.all(),
        required=False,
        empty_label='Toți clienții'
    )