from django.db import models

from employees.models import Employee

class Salary(models.Model):
    employee =  models.ForeignKey(Employee, on_delete=models.CASCADE)
    base_salary = models.DecimalField(max_digits=10,  decimal_places=2)
    bonus = models.DecimalField(max_digits=10, decimal_places=2)
    deduction = models.DecimalField(max_digits=10, decimal_places=2)
    overtime_pay = models.DecimalField(max_digits=10, decimal_places=2)
    net_salary = models.DecimalField(max_digits=10, decimal_places=2)
    pay_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
    
    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name} - {self.base_salary}"
    
    
    
class Benefits(models.Models):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    health_insurance = models.BooleanField(default=False)
    retirement_contribution = models.DecimalField(max_digits=10, decimal_places=2)
    
    