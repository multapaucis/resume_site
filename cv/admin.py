from django.contrib import admin
from cv.models import Job, JobDescription, Education, Skill

admin.site.register(Job)
admin.site.register(JobDescription)
admin.site.register(Education)
admin.site.register(Skill)
# Register your models here.
