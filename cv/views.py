from django.shortcuts import render

# Create your views here.
def index(request):
	'''The home page for the Resume'''
	return render(request, 'cv/index.html')