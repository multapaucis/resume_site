'''Define url patterns for CV App'''

from django.urls import path
from . import views

app_name = 'cv'

urlpatterns = [
    #home page
    path('', views.index, name='index'),
]