from django.contrib import admin

from .models import Salary, Benefits, PayrollRecord, Deduction

admin.site.register(Salary)
admin.site.register(Benefits)
admin.site.register(PayrollRecord)
admin.site.register(Deduction)