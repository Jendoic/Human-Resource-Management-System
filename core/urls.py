from django.contrib import admin
from django.urls import path, include
version = 'api/v1/'
urlpatterns = [
    path('admin/', admin.site.urls),
    path(f"{version}", include('authentication.urls')),
    path(f"{version}", include('employees.urls')),
    path(f"{version}/attendance/", include('attendance.urls')),
    path(f"{version}", include('leave_management.urls')),
]
