from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('adminHome')
            else:
                login(request, user)
                return redirect('home')
        else:
            context = {'error_message': 'Invalid login credentials'}
            return render(request, 'login.html', context)
    else:
        return render(request, 'userAuth/login.html')
