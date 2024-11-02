from rest_framework import serializers

from .models import Attendance
from authentication.models import CustomUser as User


class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email')
        
        
class AttendanceSerializer(serializers.ModelSerializer):
    employee = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    
    class Meta:
        model = Attendance
        fields = "__all__"