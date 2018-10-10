from django.db import models

# Create your models here.
class Job(models.Model):
	"""Previous Jobs"""
	title = models.CharField(max_length=200)
	date_started = models.DateField()
	date_finished = models.DateField()
	location = models.CharField(max_length=200)
	company = models.CharField(max_length=200)
	
	def getDescriptions(self):
		return JobDescription.objects.filter(job_title=self)

	descriptions = property(getDescriptions)
	
	def __str__(self):
		'''Returns a string with the Job Title'''
		return self.title
		
class JobDescription(models.Model):
	"""Job Descriptors"""
	job_title = models.ForeignKey(Job, on_delete=models.PROTECT)
	description = models.TextField()
	
	def __str__(self):
		'''Returns a string representing the model'''
		return self.description[:50] + "..."

class Education(models.Model):
	"""Previous Schools"""
	school_name = models.CharField(max_length=200)
	date_started = models.DateField()
	date_finished = models.DateField()
	location = models.CharField(max_length=200)
	degree = models.CharField(max_length=200)
	
	class Meta:
		verbose_name_plural = 'Education'
		
	def __str__(self):
		'''Returns a string with the School Nme'''
		return self.school_name


class SkillType(models.Model):
	"""Releveant Skills"""
	type_name = models.CharField(max_length=200)

	def getSkills(self):
		return Skill.objects.filter(stype=self)

	skills = property(getSkills)
	
	def __str__(self):
		'''Returns a string representing the Skill Type'''
		return self.type_name

class Skill(models.Model):
	"""Relevant Skills"""
	skill_name = models.CharField(max_length=200)
	stype = models.ForeignKey(SkillType, on_delete=models.PROTECT)
	
	def __str__(self):
		'''Returns a string representing the Skill'''
		return self.skill_name

class Resume(models.Model):
	"""PDF Version of the Resume"""
	res_name = models.CharField(max_length=200)
	file = models.FileField(upload_to='cv/docs/')
	
	def __str__(self):
		'''Returns a string representing the Resume'''
		return self.res_name

class Interest(models.Model):
	"""Model for my Interests"""
	interest_name = models.CharField(max_length=200)
	description = models.TextField()
	
	def __str__(self):
		'''Returns a string representing the Interest'''
		return self.interest_name
		