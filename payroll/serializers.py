from rest_framework import serializers

from .models import Salary, Benefits, Deduction, PayrollRecord

from employees.models import Employee


class SimpleEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'email')


class  SalarySerializer(serializers.ModelSerializer):
    employee = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all())
    total_salary = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Salary
        fields = "__all__"
   
    def validate_employee(self, value):
        if not Employee.objects.filter(pk=value.pk).exists():
            raise serializers.ValidationError("The specified employee does not exist.")
        return value
    
    


class DeductionSerializer(serializers.ModelSerializer):
    employee = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all())
    total_deductions = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    class Meta:
        model = Deduction
        fields = "__all__"




class BenefitsSerializer(serializers.ModelSerializer):
    employee = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all())
    class Meta:
        model = Benefits
        fields = "__all__"
        
    
class  PayrollRecordSerializer(serializers.ModelSerializer):
    employee = SimpleEmployeeSerializer(read_only=True)
    class Meta:
        model = PayrollRecord
        fields = "__all__"
        
        
        