from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class RechercheForm(forms.Form):
    mot = forms.CharField(max_length=100)
 #   message = forms.CharField(widget=forms.Textarea)
 #   envoyeur = forms.EmailField(label="Votre adresse mail")
 #   renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)

 
class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)




