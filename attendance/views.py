from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from django.utils import timezone


from employees.models import Employee
from .models import Attendance
from .serializers import AttendanceSerializer

class AttendancesView(generics.ListAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        if self.request.user.employee.designation.name == "Human Resource":
            return self.queryset.all()
        return self.queryset.filter(employee__user=self.request.user)
       
       
        

class ClockInView(APIView):
    def post(self, request):
        user = request.user
        try:
            employee = Employee.objects.get(user=user)  
        except  Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        
     
        attendance, created = Attendance.objects.get_or_create(
            employee=employee,
            clock_out__isnull=True
        )
        
        if not created:
            return Response({"message": "Already clocked in."}, status=status.HTTP_400_BAD_REQUEST)

        attendance.clock_in = timezone.now()
        attendance.save()
        return Response({"message": "Clocked in successfully."}, status=status.HTTP_200_OK)
    

class ClockOutView(APIView):
    def post(self, request):
        user = request.user
        try:
            employee = Employee.objects.get(user=user)  
        except  Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            
            attendance = Attendance.objects.get(employee=employee, clock_out__isnull=True)
            attendance.clock_out = timezone.now()
            attendance.save()  
            return Response({"message": "Clocked out successfully.", "work_hours": attendance.work_hours}, status=status.HTTP_200_OK)
        except Attendance.DoesNotExist:
            return Response({"message": "No active clock-in found."}, status=status.HTTP_400_BAD_REQUEST)
