from django import forms
from .models import Utilizator

#model-form pe Utilizator
class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(label='Parola', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma parola', widget=forms.PasswordInput)

    class Meta:
        model = Utilizator
        fields = ('username',)

    #valideaza ca parolele coincid
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Parolele nu coincid")
        return password2

    #salveaza parola
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

#permite editarea campurilor de profil
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Utilizator
        fields = ('username',)