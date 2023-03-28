from django.shortcuts import render

# home- dashboard
def dashboard(request):
    context = {}
    return render(request, 'base_users/home.html', context)

# profile settings
def setting(request):
    context = {}
    return render(request, 'base_users/settings.html', context)

# calender
def calender(request):
    context = {}
    return render(request, 'base_users/calender.html', context)

# monthly report
def monthly(request):
    context = {}
    return render(request, 'base_users/monthly.html', context)

# yearly report
def yearly(request):
    context = {}
    return render(request, 'base_users/yearly.html', context)