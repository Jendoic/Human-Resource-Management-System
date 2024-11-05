from django.db import models

from employees.models import Employee



class Salary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="salary")
    base_salary = models.DecimalField(max_digits=10, decimal_places=2)
    overtime_pay = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    bonus = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_salary = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        self.total_salary = self.base_salary + self.overtime_pay + self.bonus
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Salary id {self.id} | {self.employee}'s Salary"


class Deduction(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="deductions")
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    other_deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_deductions = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        self.total_deductions = self.tax + self.other_deductions
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee}'s Deductions"


class Benefits(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="benefits")
    healthcare = models.BooleanField(default=False)
    retirement_plan = models.BooleanField(default=False)
    other_benefits = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.employee}'s Benefits"


class PayrollRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="payroll_records")
    payroll_date = models.DateField(auto_now_add=True)
    unique_id = models.CharField(max_length=100, unique=True)
    net_pay = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending')



    def __str__(self):
        return f"Payroll for {self.employee.first_name} on {self.payroll_date}"
