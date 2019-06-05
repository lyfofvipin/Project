from django import forms
from .models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()

class UserDetailUpdateForm(forms.ModelForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class UserProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ["Profile_pic"]
        