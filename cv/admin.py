from django.contrib import admin
from cv.models import Job, JobDescription, Education, Skill, Resume

# Register your models here.
admin.site.register(Job)
admin.site.register(JobDescription)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Resume)

