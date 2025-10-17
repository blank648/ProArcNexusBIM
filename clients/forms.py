from django import forms
from .models import Client

#model-form pentru client
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['denumire', 'cui', 'adresa', 'telefon', 'email']
        widgets = {
            'adresa': forms.Textarea(attrs={'rows': 2}),
        }