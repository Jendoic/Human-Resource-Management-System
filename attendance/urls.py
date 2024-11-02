from django.urls import path
from .views import AttendancesView, ClockInView, ClockOutView

urlpatterns = [
    path('', AttendancesView.as_view(), name='attendance'),
    path('clock-in/', ClockInView.as_view(), name='clock_in'),
    path('clock-out/', ClockOutView.as_view(), name='clock_out'),
]
