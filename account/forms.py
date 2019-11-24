from django import forms
from .models import UserProfil


class LogInForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

class UserProfilForm(forms.ModelForm):
    class Meta:
        user_profil = UserProfil
        fields = ('date_of_birth',)



