from rest_framework import serializers

from .models import PerformanceGoal, ReviewComment
from employees.models import Employee





class PerformanceGoalSerializer(serializers.ModelSerializer):
    employee = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all())
    class Meta:
        model = PerformanceGoal
        fields = '__all__'
        
        
class ReviewCommentSerializer(serializers.ModelSerializer):
    employee = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all())
    review_by = serializers.PrimaryKeyRelatedField()
    class Meta:
        model = ReviewComment
        fields = '__all__'