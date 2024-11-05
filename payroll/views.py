from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from django.utils import timezone

from employees.models import Employee

from .models import PayrollRecord, Salary, Deduction, Benefits
from .serializers import PayrollRecordSerializer, SalarySerializer, DeductionSerializer, BenefitsSerializer
from .permissions import IsHumanResourceAdmin
from django.shortcuts import get_object_or_404

from django.utils import timezone

class PayrollViewSet(viewsets.ModelViewSet):
    serializer_class = PayrollRecordSerializer
    queryset = PayrollRecord.objects.all()
    permission_classes = [IsHumanResourceAdmin]

    def generate_unique_id(self, employee_id, payroll_period):
        return f"{employee_id}-{payroll_period}"

    def create(self, request, *args, **kwargs):
        payroll_records = []
        payroll_period = timezone.now().strftime("%Y-%m") 

        for employee in Employee.objects.all():
            unique_id = self.generate_unique_id(employee.id, payroll_period)

           
            if PayrollRecord.objects.filter(unique_id=unique_id).exists():
                continue 

            salary = employee.salary.first() 
            deductions = employee.deductions.first() 
            print("salary: ", salary)
            print("deduction: ", deductions) 
            if salary and deductions:  
                total_salary = salary.total_salary
                print("Total salary: ", total_salary)
                total_deductions = deductions.total_deductions
                net_pay = total_salary - total_deductions

                
                payroll_record = PayrollRecord(
                    employee=employee,
                    unique_id=unique_id, 
                    net_pay=net_pay,
                    status='completed'
                )
                payroll_record.save()
                payroll_records.append(payroll_record)

        serializer = PayrollRecordSerializer(payroll_records, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

 


class SalaryViewSet(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
    
    print(Salary.objects.filter(id=5))
   
    def get_queryset(self):
        if self.request.user.employee.designation.name == "Human Resource":
            return self.queryset
        else:

            return self.queryset.filter(employee=self.request.user.employee)
    
    
    def create(self, request, *args, **kwargs):
        employee_id = request.data.get('employee')
        if Salary.objects.filter(employee=employee_id).exists():
            return Response(
                {"error":"Salary for this employee already exists, Use update instead"},
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().create(request,  *args, **kwargs)
   
        
        
    

class DeductionViewSet(viewsets.ModelViewSet):
    serializer_class = DeductionSerializer
    queryset = Deduction.objects.all()
    
    def get_queryset(self):
        if self.request.user.employee.designation.name == "Human Resource":
            return self.queryset
        else:

            return self.queryset.filter(employee=self.request.user.employee)
        
    def create(self, request, *args, **kwargs):
        employee_id = request.data.get('employee')
        if Deduction.objects.filter(employee=employee_id).exists():
            return Response(
                {"error":"Deduction for this employee already exists, Use update instead"},
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().create(request,  *args, **kwargs)
    
    
    
class BenefitViewSet(viewsets.ModelViewSet):
    serializer_class = BenefitsSerializer
    queryset = Benefits.objects.all()
    
    def get_queryset(self):
        if self.request.user.employee.designation.name == "Human Resource":
            return self.queryset
        else:

            return self.queryset.filter(employee=self.request.user.employee)
        
    