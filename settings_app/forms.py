from django import forms
from .models import SetareGenerala

class SetareGeneralaForm(forms.ModelForm):
    class Meta:
        model = SetareGenerala
        fields = ['cheie', 'valoare']
        widgets = {
            'valoare': forms.Textarea(attrs={'rows': 3}),
        }
