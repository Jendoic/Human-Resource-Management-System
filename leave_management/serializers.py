from rest_framework import serializers

from .models import Leave
from authentication.models import CustomUser as User

class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email')

class LeaveSerializer(serializers.ModelSerializer):
    employee = SimpleUserSerializer(read_only=True)
    
    class Meta:
        model = Leave
        fields = '__all__'  
        
    def create(self, validated_data):
        # Set employee to the logged-in user
        validated_data['employee'] = self.context['request'].user
        return super().create(validated_data)