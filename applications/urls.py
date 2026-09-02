from rest_framework.routers import  DefaultRouter
from .views import CompanyViewSet,ApplicationViewSet,InterviewRoundViewSet
from .views import application_list_view, dashboard_view, add_application_view, edit_application_view, delete_application_view, interviewround_list_view, add_interviewround_view, edit_interviewround_view, delete_interviewround_view
from django.urls import path

router = DefaultRouter()
router.register(r'company', CompanyViewSet)
router.register(r'application', ApplicationViewSet)
router.register(r'interviewround', InterviewRoundViewSet)

urlpatterns = router.urls + [
    path('applications-page/', application_list_view, name='application_list'),
    path('dashboard-page/', dashboard_view, name='dashboard'),
    path('add-application/', add_application_view, name='add_application'),
    path('edit-application/<int:pk>/', edit_application_view, name='edit_application'),
    path('delete-application/<int:pk>/', delete_application_view, name='delete_application'),
    path('interviewround-page/', interviewround_list_view, name='interviewround_list'),
    path('add-interviewround/', add_interviewround_view, name='add_interviewround'),
    path('edit-interviewround/<int:pk>/', edit_interviewround_view, name='edit_interviewround'),
    path('delete-interviewround/<int:pk>/', delete_interviewround_view, name='delete_interviewround')
]