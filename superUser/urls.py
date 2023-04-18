from django.urls import path
from superUser import views 

urlpatterns = [
    path('', views.dashboard, name='adminHome'),
    path('users/', views.allUsers, name='adminUsers'),
    path('update-user/<str:pk>/', views.updateUser, name='update-user'),
    path('delete-user/<str:pk>/', views.deleteUser, name='delete-user'),
    path('profile/', views.setting, name='adminProfile'),
    path('calender/', views.calender, name='adminCalender'),
    path('monthly-report/', views.monthly, name='adminMonthly'),
    path('yearly-report/', views.yearly, name='adminYearly'),
]