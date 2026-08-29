from rest_framework import viewsets
from .models import Company,Application,InterviewRound
from .serializers import CompanySerializer,ApplicationSerializer,InterviewRoundSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'company']

    @action(detail=False, methods=['get'])
    def stats(self, request):
        total = Application.objects.count()
        applied_count = Application.objects.filter(status='applied').count()
        interview_count = Application.objects.filter(status='interview').count()
        offer_count = Application.objects.filter(status='offer').count()
        reject_count = Application.objects.filter(status='reject').count()

        stats_data = {
            'total_applications': total,
            'applied': applied_count,
            'interview': interview_count,
            'offer': offer_count,
            'reject': reject_count,
            }
        return Response(stats_data)

class InterviewRoundViewSet(viewsets.ModelViewSet):
    queryset = InterviewRound.objects.all()
    serializer_class = InterviewRoundSerializer


def application_list_view(request):
    applications = Application.objects.all()
    context = {'applications': applications}
    return render(request, 'applications/application_list.html', context)

def dashboard_view(request):
    applications = Application.objects.all()
    total = Application.objects.count()
    applied_count = Application.objects.filter(status='applied').count()
    interview_count = Application.objects.filter(status='interview').count()
    offer_count = Application.objects.filter(status='offer').count()
    reject_count = Application.objects.filter(status='reject').count()
    context = {
        'total': total,
        'applied_count': applied_count,
        'interview_count': interview_count,
        'offer_count': offer_count,
        'reject_count': reject_count,
        }
    return render(request, 'applications/dashboard.html',context)