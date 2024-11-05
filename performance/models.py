from django.db import models

from employees.models import Employee
class PerformanceGoal(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='performance_goal')
    goal = models.CharField(max_length=255)
    metrics = models.TextField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('achieved', 'Achieved')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"{self.employee}'s Goal: {self.goal}"
    
    
    
class ReviewComment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="review_comments")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    reviewed_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)