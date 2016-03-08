from django import forms
from django.contrib.auth.forms import UserCreationForm


class ProfileUserForm(UserCreationForm):

    first_name = forms.CharField(max_length=32)
    last_name = forms.CharField(max_length=32)
    origin = forms.CharField(max_length=64)
    dream_location = forms.CharField(max_length=64)
    age = forms.IntegerField(required=True)
