from django.db import models
from profiles.models import Profile
from experiments.models import Experiment

FILE_FORMATS = (('txt', 'Claris Text Format'), ('ziptxt', 'Zipped text format'), ('nc', 'netcdf'))
SUBMISSION_MODES = (('POST', 'HTTP POST'), ('PUT', 'FTP PUT'))
FREQUENCIES = (('day', 'daily data'), ('month', 'monthly data'))


class Model(models.Model):

	slug = models.SlugField()
	title  = models.CharField(max_length=50, default="")
	contact = models.ForeignKey(Profile)
	description = models.TextField(default="", blank=True)

	def __unicode__(self):
		return self.title

class Variable(models.Model):

	short_name = models.CharField(max_length=20)
	standard_name = models.CharField(max_length=50)
	long_name = models.CharField(max_length=50)
	units = models.CharField(max_length=20)

class Submission(models.Model):

	owner = models.ForeignKey(Profile)			# Who owns this submission

	experiment = models.ForeignKey(Experiment, null=True)

	model = models.ForeignKey(Model)
	version = models.IntegerField(default=1)

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField()
	
	notes = models.TextField(blank=True, default='')

	archive_path = models.CharField(max_length=500, default='', blank=True)
	archive_filename = models.CharField(max_length=500, default='', blank=True)

	def __unicode__(self):
		return "{} | {} version {}".format(self.model, self.experiment, self.version)

class Upload(models.Model):

	timestamp = models.DateTimeField(null=True)
	submission = models.ForeignKey(Submission, related_name='uploads')

	format = models.CharField(max_length=10, choices=FILE_FORMATS, default='txt')
	mode = models.CharField(max_length=10, choices=SUBMISSION_MODES, default='POST')
	path = models.CharField(max_length=500, default='', blank=True)
	filename = models.CharField(max_length=500, default='', blank=True)

