from django.utils import timezone
from django.db import models

from employees.models import Employee


class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    clock_in = models.DateTimeField(null=True, blank=True)
    clock_out = models.DateTimeField(null=True, blank=True)
    work_hours = models.DurationField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Attendance'
        verbose_name_plural = 'Attendances'
        

        
    def save(self, *args, **kwargs):
        if self.clock_in and self.clock_out:
            self.work_hours = self.clock_out - self.clock_in
            
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"Attendance record for {self.employee.first_name} {self.employee.last_name}"
    
    