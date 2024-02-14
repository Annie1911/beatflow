from django import forms
from .models import Profile

class InscriptionForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Profile
        fields = ['nom_profile', 'abonnements']

    def clean(self):
        cleaned_data = super().clean()
        nom_profile = cleaned_data.get("nom_profile")
        abonnements = cleaned_data.get("abonnements")

        if not nom_profile:
            raise forms.ValidationError(
                "Le champ Nom de profil est requis."
            )

        if not abonnements:
            raise forms.ValidationError(
                "Le champ Abonnements est requis."
            )