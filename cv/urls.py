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
]