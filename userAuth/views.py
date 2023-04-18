from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib import messages

# login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                if user.is_superuser:
                    login(request, user)
                    return redirect('adminHome')
                else:
                    login(request, user)
                    return redirect('home')
            else:
                messages.error(request, 'Your account is inactive. Please contact an administrator.')
                return redirect('login')
        else:
            context = {'error_message': 'Invalid login credentials'}
            return render(request, 'userAuth/login.html', context)
    else:
        return render(request, 'userAuth/login.html')


# logout views
def logout_view(request):
    logout(request)
    return redirect('login')