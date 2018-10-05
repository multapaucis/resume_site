'''Define url patterns for CV App'''

from django.urls import path
from . import views

app_name = 'cv'

urlpatterns = [
    #home page
    path('', views.index, name='index'),
    #show all work experience
    path('jobs', views.jobs, name='jobs'),
    #show all education
    path('education', views.education, name='education'),
    #show all skills
    path('skills' , views.skills, name='skills'),
    #contact information
    path('contact' , views.contact, name='contact'),
    #Provide a preview of the PDF Version of Resume and option toDownload
    path('download' , views.download, name='download'),
    #Provide a PDF Version of Resume for View and Download
    path('downloadPDF' , views.downloadPDF, name='downloadPDF'),
]