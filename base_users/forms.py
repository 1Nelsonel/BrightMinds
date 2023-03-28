from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import UserProfile


class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    mobile_number = forms.CharField(max_length=20, required=True)
    id_number = forms.CharField(max_length=20, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'mobile_number', 'id_number')


class UserProfileForm(forms.ModelForm):
    mobile_number = forms.CharField(max_length=20, required=True)
    id_number = forms.CharField(max_length=20, required=True)

    class Meta:
        model = UserProfile
        fields = ('mobile_number', 'id_number')
