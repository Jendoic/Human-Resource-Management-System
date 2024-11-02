from rest_framework.permissions import BasePermission
from .models import Employee

class IsHumanResourceAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.employee.designation.name == "Human Resource"


# class  IsEmployee(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return obj.user == request.user