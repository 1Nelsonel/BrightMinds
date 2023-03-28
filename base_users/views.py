from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render



# home- dashboard
@login_required(login_url='login')
def dashboard(request):
    context = {}
    return render(request, 'base_users/home.html', context)

# profile settings
@login_required(login_url='login')
def setting(request):
    context = {}
    return render(request, 'base_users/settings.html', context)

# calender
@login_required(login_url='login')
def calender(request):
    context = {}
    return render(request, 'base_users/calender.html', context)

# monthly report
@login_required(login_url='login')
def monthly(request):
    context = {}
    return render(request, 'base_users/monthly.html', context)

# yearly report
@login_required(login_url='login')
def yearly(request):
    context = {}
    return render(request, 'base_users/yearly.html', context)