from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.hashers import make_password

from .forms import UserSignUpForm, UserProfileForm
from base_users.models import UserProfile
from django.contrib.auth.models import User


# add users
@login_required
def allUsers(request):
    if not request.user.is_superuser:
        messages.error(request, "You don't have permission to create users.")
        return redirect('home')

    if request.method == 'POST':
        user_form = UserSignUpForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.password = make_password(profile_form.cleaned_data['id_number'])
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            username = user.username
            email = user.email
            password = profile_form.cleaned_data['id_number']

            send_mail(
                'Your login credentials',
                f'Username: {username}\nPassword: {password}',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )

            messages.success(request, f'{username} created successfully! Login credentials sent to {email}.')
            return redirect('create_user')
    else:
        user_form = UserSignUpForm()
        profile_form = UserProfileForm()
    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'superUser/users.html', context)


# home- dashboard
def dashboard(request):
    context = {}
    return render(request, 'superUser/home.html', context)

# profile settings
def setting(request):
    context = {}
    return render(request, 'superUser/settings.html', context)

# calender
def calender(request):
    context = {}
    return render(request, 'superUser/calender.html', context)

# monthly report
def monthly(request):
    context = {}
    return render(request, 'superUser/monthly.html', context)

# yearly report
def yearly(request):
    context = {}
    return render(request, 'superUser/yearly.html', context)



# @login_required
# def home(request):
#     return render(request, 'home.html')
