from django.contrib.auth import get_user_model
from django.contrib import messages
from django.shortcuts import redirect, render
from django.conf import settings
import random
import string

from .forms import UserSignUpForm
from base_users.models import UserProfile
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

User = get_user_model()


def superuser_required(function=None, redirect_field_name='next', login_url='login'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_superuser,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


# create user
@superuser_required
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

@superuser_required
def updateUser(request, pk):
    user = User.objects.get(id=pk)
    try:
        profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=user)

    if request.method == 'POST':
        form = UserSignUpForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            # Get the UserProfile instance for the user, or create a new one if it doesn't exist
            profile, created = UserProfile.objects.get_or_create(user=user)

            # Update the profile data with the form data
            profile.mobile_number = form.cleaned_data['mobile_number']
            profile.id_number = form.cleaned_data['id_number']
            # profile.status = form.cleaned_data['status']
            profile.save()

            messages.success(request, 'User updated successfully!')
            return redirect('adminUsers')

    else:
        initial = {
            'mobile_number': profile.mobile_number,
            'id_number': profile.id_number,
            # 'status': user.is_active,
        }
        form = UserSignUpForm(instance=user, initial=initial)
    
    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'superUser/editUser.html', context)



# home- dashboard
@superuser_required
def dashboard(request):
    context = {}
    return render(request, 'superUser/home.html', context)

# profile settings
@superuser_required
def setting(request):
    context = {}
    return render(request, 'superUser/settings.html', context)

# calender
@superuser_required
def calender(request):
    context = {}
    return render(request, 'superUser/calender.html', context)

# monthly report
@superuser_required
def monthly(request):
    context = {}
    return render(request, 'superUser/monthly.html', context)

# yearly report
@superuser_required
def yearly(request):
    context = {}
    return render(request, 'superUser/yearly.html', context)
