from django.shortcuts import render

from .models import Job, JobDescription, Education, Skill

# Create your views here.
def index(request):
	'''The home page for the Resume'''
	return render(request, 'cv/index.html')

def jobs(request):
	'''Show all Work Experience'''
	jobs = Job.objects.order_by('-date_started')
	'''descriptions = {}
	for job in jobs:
		d = JobDescription.objects.filter(job_title=job.id)
		descriptions[job.id] = d
	'''
	context = {'jobs': jobs}
	return render(request, 'cv/jobs.html', context)

def education(request):
	'''Show all Education'''
	education = Education.objects.order_by('-date_started')
	context = {'education': education}
	return render(request, 'cv/education.html', context)

def skills(request):
	'''Show all Skills'''
	skills = Skill.objects.order_by('skill_type')
	context = {'skills': skills}
	return render(request, 'cv/skills.html', context)