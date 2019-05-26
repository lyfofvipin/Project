from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):

    email = forms.EmailField()
    pet_name = forms.CharField(max_length=30)

    class Meta:
        
        model = User
        fields = ['username', 'email', 'pet_name', 'password1', 'password1']