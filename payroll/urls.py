from rest_framework.routers import DefaultRouter
from .views import PayrollViewSet, SalaryViewSet, DeductionViewSet, BenefitViewSet

router = DefaultRouter()
router.register(r'payroll', PayrollViewSet)
router.register(r'salary', SalaryViewSet)
router.register(r'deduction', DeductionViewSet)
router.register(r'benefit', BenefitViewSet)

urlpatterns = router.urls