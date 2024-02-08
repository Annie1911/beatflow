from django import forms
from .models import Profile

class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nom_profile', 'abonnements']