from django.contrib import admin

from performance.models import PerformanceGoal, ReviewComment


admin.site.register(PerformanceGoal)
admin.site.register(ReviewComment)
