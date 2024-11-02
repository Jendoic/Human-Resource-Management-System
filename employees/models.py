from django.db import models

from authentication.models import CustomUser
from utils.choices import GENDER_CHOICES, EMPLOYEE_STATUS

class Department(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.id} | {self.name}" 
    
class Designation(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.id} | {self.name}" 
    
    

class Employee(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='employee', null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    mobile = models.CharField(max_length=100, null=True)
    emp_code = models.CharField(max_length=100, null=True, unique=True)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(choices=GENDER_CHOICES, null=True, max_length=50)
    nationality = models.CharField(max_length=100, null=True)
    date_joined = models.DateField(null=True)
    date_end = models.DateField(null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    designation = models.ForeignKey(Designation, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    emergency_mobile = models.CharField(max_length=100, null=True)
    status =  models.CharField(max_length=100, choices=EMPLOYEE_STATUS, null=True)
    
    def save(self, *args, **kwargs):
        if not self.emp_code:
            employee_count = Employee.objects.count() + 1
            self.emp_code = f"EMP{employee_count:03}"
        super().save(*args, **kwargs)
    
    def __str__(self):
        if self.first_name and self.last_name:
            return f" {self.id} {self.first_name} {self.last_name} | ({self.emp_code}) of {self.department}"
        return f"{self.user} profile"
    

  