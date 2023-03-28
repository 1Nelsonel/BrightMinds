from django.urls import path
from userAuth import views


urlpatterns = [
    path('', views.login_view, name='login'),
   
]