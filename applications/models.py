from django.db import models

# Create your models here.
STATUS_CHOICES = [
    ('applied', 'Applied'),
    ('interview', 'Interview'),
    ('reject', 'Reject'),
    ('offer', 'Offer'),
]

ROUND_TYPE_CHOICES =[
    ('HR', 'HRRound'),
    ('Technical', 'TechnicalRound'),
    ('Final', 'FinalRound'),
    ('Managerial', 'ManagerialRound'),
]

class Company(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField(blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Application(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100, blank=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, blank=False)
    applied_date = models.DateField(blank=False)
    deadline = models.DateField(blank=True, null=True)
    salary_range = models.CharField(max_length=50, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
            return self.job_title

class InterviewRound(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    round_type = models.CharField(max_length=50, choices=ROUND_TYPE_CHOICES)
    date = models.DateTimeField(blank=False)
    feedback = models.TextField(blank=True)

    def __str__(self):
        return self.round_type