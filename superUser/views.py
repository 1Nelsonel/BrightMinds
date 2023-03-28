from django.contrib.auth import get_user_model
from django.contrib import messages
from django.shortcuts import redirect, render
from django.conf import settings
import random
import string

from .forms import UserSignUpForm
from base_users.models import UserProfile
from django.core.mail import send_mail

User = get_user_model()

# create user


def allUsers(request):
    allusers = User.objects.all()
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=12))
            user.set_password(password)
            user.save()

            # Check if a UserProfile instance with the same user_id already exists in the database
            profile = UserProfile.objects.filter(user=user).first()

            if profile:
                # If a profile exists, update its data
                profile.mobile_number = form.cleaned_data['mobile_number']
                profile.id_number = form.cleaned_data['id_number']
                profile.save()
            else:
                # Otherwise, create a new profile
                profile = UserProfile(user=user, mobile_number=form.cleaned_data['mobile_number'], id_number=form.cleaned_data['id_number'])
                profile.save()

            # Send email to the new user with login credentials
            subject = 'BrightMinds login credentials'
            message = f'Hello {user.first_name} {user.last_name} Your BrightMind Group has been created,\n\nYou can login to your account with the following credentials:\n\nUsername: {user.username}\nPassword: {password}\n\nThank you!'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail(subject, message, email_from, recipient_list)
            # code for sending email

            messages.success(request, 'User created successfully!')
            return redirect('adminUsers')

    else:
        form = UserSignUpForm()

    context = {
        'form': form,
        'allusers': allusers,
    }
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
