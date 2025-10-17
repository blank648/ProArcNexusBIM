from django import forms
from .models import Articol

#model-form
class ArticolForm(forms.ModelForm):
    class Meta:
        model = Articol
        fields = [
            'cod', 'denumire', 'um', 'pret_standard'
        ]
        widgets = {
            'denumire': forms.TextInput(attrs={'size':40}),
            'pret_standard': forms.TextInput(attrs={'step':'0.01'}),
        }