from rest_framework import viewsets, filters
from .models import Company,Application,InterviewRound
from .serializers import CompanySerializer,ApplicationSerializer,InterviewRoundSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render, redirect
from .forms import ApplicationForm, InterviewRoundForm

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status', 'company']
    search_fields = ['job_title', 'notes']

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
    search_query = request.GET.get('search', '')
    applications = Application.objects.all()
    if search_query:
        applications = applications.filter(job_title__icontains=search_query)
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

def add_application_view(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('application_list')
    else:
        form = ApplicationForm()
    return render(request, 'applications/application_form.html', {'form': form})

def edit_application_view(request, pk):
    application = Application.objects.get(pk=pk)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('application_list')
    else:
        form = ApplicationForm(instance=application)
    return render(request, 'applications/application_form.html', {'form': form})

def delete_application_view(request, pk):
    application = Application.objects.get(pk=pk)
    application.delete()
    return redirect('application_list')

def interviewround_list_view(request):
    interviewrounds = InterviewRound.objects.all()
    context = {'interviewrounds': interviewrounds}
    return render(request, 'applications/interviewround_list.html', context)

def add_interviewround_view(request):
    if request.method == 'POST':
        form = InterviewRoundForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('interviewround_list')
    else:
        form = InterviewRoundForm()
    return render(request, 'applications/interviewround_form.html', {'form': form})

def edit_interviewround_view(request, pk):
    interviewround = InterviewRound.objects.get(pk=pk)
    if request.method == 'POST':
        form = InterviewRoundForm(request.POST, instance=interviewround)
        if form.is_valid():
            form.save()
            return redirect('interviewround_list')
    else:
        form = InterviewRoundForm(instance=interviewround)
    return render(request, 'applications/interviewround_form.html', {'form': form})

def delete_interviewround_view(request, pk):
    interviewround = InterviewRound.objects.get(pk=pk)
    interviewround.delete()
    return redirect('interviewround_list')