from django.shortcuts import render

from .models import Job, JobDescription

# Create your views here.
def index(request):
	'''The home page for the Resume'''
	return render(request, 'cv/index.html')

def jobs(request):
	'''SHow all Work Experience'''
	jobs = Job.objects.order_by('date_started')
	descriptions = JobDescription.objects
	context = {'jobs': jobs, 'descriptions': descriptions}
	return render(request, 'cv/jobs.html', context)