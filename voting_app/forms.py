from django import forms
from voting_app.models import *

class UserForm(forms.ModelForm):
    password=forms.CharField(max_length=50, required=True, widget=forms.PasswordInput,label="Enter Password here")
    class Meta:
        model=User
        fields=('username','email','password')

class VoterForm(forms.ModelForm):
    class Meta:
        model=VoterDetails
        fields=('Constituency',)
        
class ConForm(forms.ModelForm):
    class Meta:
        model=Constituency
        fields="__all__"