from django.test import TestCase
from .models import Company, Application

# Create your tests here.
class ApplicationModelTest(TestCase):
    def test_application_creation(self):
        company = Company.objects.create(name='Test Company')
        application = Application.objects.create(
            company=company,
            job_title='Test Job',
            status='applied',
            applied_date='2026-08-01'
        )
        self.assertEqual(application.job_title, 'Test Job')

    def test_stats_endpoint(self):
        company = Company.objects.create(name='Test Company')
        Application.objects.create(company=company, job_title='Job 1', status='applied', applied_date='2026-08-01')
        Application.objects.create(company=company, job_title='Job 2', status='interview', applied_date='2026-08-02')
    
        response = self.client.get('/application/stats/')
        self.assertEqual(response.status_code, 401)