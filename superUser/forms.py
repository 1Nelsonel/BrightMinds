from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from base_users.models import UserProfile

class UserSignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your username', 'required': True}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter email', 'required': True}))
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter first name', 'required': True}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter last name', 'required': True}))
    mobile_number = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter mobile number', 'required': True}))
    id_number = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter ID number', 'required': True}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name',  'mobile_number', 'id_number')

class UserProfileForm(forms.ModelForm):
    mobile_number = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter mobile number', 'required': True}))
    id_number = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter ID number', 'required': True}))

    class Meta:
        model = UserProfile
        fields = ('mobile_number', 'id_number')
