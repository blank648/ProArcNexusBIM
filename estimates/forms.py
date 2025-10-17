from django import forms
from django.forms import inlineformset_factory
from .models import Deviz, LinieDeviz

class DevizForm(forms.ModelForm):
    class Meta:
        model = Deviz
        fields = ['numar_deviz', 'data_emitere', 'client', 'status']

class LinieDevizForm(forms.ModelForm):
    class Meta:
        model = LinieDeviz
        fields = ['articol', 'cantitate', 'pret_unitar']

#inline formset
LinieDevizFormSet = inlineformset_factory(
    Deviz,LinieDeviz,
    form=LinieDevizForm,
    extra=1,can_delete=True
)
