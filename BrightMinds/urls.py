from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base_users.urls')),
    path('superUser/', include('superUser.urls')),

]
