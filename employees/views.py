from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Department, Designation, Employee
from .serializers import DepartmentSerializer, DesignationSerializer, EmployeeSerializer



class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    
    
    def get_queryset(self):
        if self.request.user.employee.designation.name == "Human Resource":
            return self.queryset
    
        return self.queryset.filter(user=self.request.user)
    