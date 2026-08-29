from rest_framework.routers import  DefaultRouter
from .views import CompanyViewSet,ApplicationViewSet,InterviewRoundViewSet
from .views import application_list_view, dashboard_view
from django.urls import path

router = DefaultRouter()
router.register(r'company', CompanyViewSet)
router.register(r'application', ApplicationViewSet)
router.register(r'interviewround', InterviewRoundViewSet)

urlpatterns = router.urls + [
    path('applications-page/', application_list_view, name='application_list'),
    path('dashboard-page/', dashboard_view, name='dashboard'),
]