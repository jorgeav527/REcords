from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile

# Form to Sing up a new user
class AccountRegister(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'gmail only!',
    }))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

# Update the account form
class AccountUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name",  "email")

# Profile form
class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ("date_of_birth", "image")