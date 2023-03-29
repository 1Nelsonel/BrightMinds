from django import forms
from django.contrib.auth.models import User
from base_users.models import UserProfile


class UserSignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your username', 'required': True}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter email', 'required': True}))
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter first name', 'required': True}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter last name', 'required': True}))
    mobile_number = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter mobile number', 'required': True}))
    id_number = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter ID number', 'required': True}))
    # is_active = forms.BooleanField(required=False, initial=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'mobile_number', 'id_number']

    def save(self, commit=True):
        user = super(UserSignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            # Create a new UserProfile instance and associate it with the user instance
            profile = UserProfile.objects.create(user=user, mobile_number=self.cleaned_data['mobile_number'], id_number=self.cleaned_data['id_number'])
            profile.save()
        return user

