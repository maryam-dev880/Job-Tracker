from django.contrib import admin
from .models import Company,Application,InterviewRound

# Register your models here.
admin.site.register(Company)
admin.site.register(Application)
admin.site.register(InterviewRound)