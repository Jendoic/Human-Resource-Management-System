from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Leave
from .serializers import LeaveSerializer 


class LeaveViewSet(viewsets.ModelViewSet):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        if self.request.user.employee.designation.name == "Human Resource":
            return self.queryset
        return self.queryset.filter(employee=self.request.user)
       
    @action(detail=False, methods=['post'])
    def request_leave(self, request):
        data = request.data
        data['employee'] = self.request.user
        serializer = self.get_serializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Leave request submitted successfully."},serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['put', 'patch'])
    def approve_leave(self, request, pk=None):
        leave = self.get_object()
        if not self.request.user.employee.designation.name == "Human Resource":
            return Response({"detail": "Not authorized to approve leave requests."}, status=status.HTTP_403_FORBIDDEN)
        
        new_status = request.data.get("status")
        if new_status in  ['approved', 'declined']:
            leave.status = new_status
            leave.save()
            return Response({"message": f"Leave request {new_status} successfully."}, status=status.HTTP_200_OK)
        return Response({"detail": "Invalid status update."}, status=status.HTTP_400_BAD_REQUEST)