from django.urls import path
from . import views 

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('profile/', views.setting, name='profile'),
    path('calender/', views.calender, name='calender'),
    path('monthly-report/', views.monthly, name='monthly'),
    path('yearly-report/', views.yearly, name='yearly'),
]