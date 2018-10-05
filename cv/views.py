from django.shortcuts import render
from django.http import FileResponse, Http404

from .models import Job, JobDescription, Education, Skill, Resume

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

def contact(request):
	'''The contact me page'''
	return render(request, 'cv/contact.html')

def download(request):
	'''Show PDF version of Resume'''
	pdfRes = Resume.objects.get(res_name="current")
	context= {"pdfRes": pdfRes}
	return render(request, 'cv/pdf.html', context)

def downloadPDF(request):
	'''Return PDF version of Resume'''
	pdfRes = Resume.objects.get(res_name="current")
	response = FileResponse(open(pdfRes.file.url, 'rb'))
	return response
