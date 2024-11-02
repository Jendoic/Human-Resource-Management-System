from django.db.models.signals import post_save
from django.dispatch import receiver

from authentication.models import CustomUser
from .models import Employee


@receiver(post_save, sender=CustomUser)
def create_employee_profile(sender, instance, created,  **kwargs):
    if created:
        Employee.objects.create(user=instance)
