from django.db import models
from django.core.files.storage import FileSystemStorage

from profiles.models import Profile
from experiments.models import Experiment

from django.conf import settings

FILE_FORMATS = (('txt', 'Claris Text Format'), ('ziptxt', 'Zipped text format'), ('nc', 'netcdf'))
SUBMISSION_MODES = (('POST', 'HTTP POST'), ('PUT', 'FTP PUT'))
FREQUENCIES = (('day', 'daily data'), ('month', 'monthly data'))
META_DEPENDENCY_CATEGORIES = (('Equal', 'equal'),)

filestorage = FileSystemStorage(settings.MEDIA_ROOT)

def make_upload_path(instance, filename):

	return "{}/{}/{}/uploaded/{}".format(instance.submission.owner.user, instance.submission.model.slug, instance.submission.experiment.slug, filename)

class Model(models.Model):

	slug = models.SlugField()
	title  = models.CharField(max_length=50, default="")
	contact = models.ForeignKey(Profile)
	description = models.TextField(default="", blank=True)

	def __unicode__(self):
		return self.title

class ModelMetaCategory(models.Model):

	slug = models.SlugField()
	description = models.TextField(default="")

class ModelMetaTerm(models.Model):

	category = models.ForeignKey(ModelMetaCategory)
	name = models.SlugField()
	long_name = models.CharField(max_length=100, default="")
	help_text = models.TextField(default="", blank=True)
	multiple = models.BooleanField(default=False)

#	depends_on = models.ForeignKey('ModelMetaDependencies') 

class ModelMetaDependencies(models.Model):

	depends_on = models.ForeignKey(ModelMetaTerm, related_name='depended_on')
	category = models.TextField(choices=META_DEPENDENCY_CATEGORIES)
	depends_value = models.ForeignKey('ModelMetaValues')

class ModelMetaValues(models.Model):

	term = models.ForeignKey(ModelMetaTerm, related_name='values')
	value = models.CharField(max_length=100)


class Submission(models.Model):

	owner = models.ForeignKey(Profile)			# Who owns this submission

	experiment = models.ForeignKey(Experiment, null=True)

	model = models.ForeignKey(Model)
	version = models.IntegerField(default=1)

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	
	notes = models.TextField(blank=True, default='')

	archive_path = models.CharField(max_length=500, default='', blank=True)
	archive_filename = models.CharField(max_length=500, default='', blank=True)

	def __unicode__(self):
		return "{} > {} ({}) version {}".format(self.experiment.meta, self.experiment, self.model, self.version)

class Upload(models.Model):

	timestamp = models.DateTimeField(auto_now_add=True)
	submission = models.ForeignKey(Submission, related_name='uploads')

	format = models.CharField(max_length=10, choices=FILE_FORMATS, default='txt')
	mode = models.CharField(max_length=10, choices=SUBMISSION_MODES, default='POST')

	path = models.CharField(max_length=500, default='', blank=True)
	filename = models.CharField(max_length=500, default='', blank=True)

	uploaded = models.FileField(null=True, storage=filestorage, upload_to=make_upload_path)

	status = models.CharField(max_length=200, blank=True, default='unknown')

	def __unicode__(self):
		return self.uploaded.url


