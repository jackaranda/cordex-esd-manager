from django.db import models
from profiles.models import Profile

FILE_FORMATS = (('txt', 'Claris Text Format'), ('ziptxt', 'Zipped text format'), ('nc', 'netcdf'))
SUBMISSION_MODES = (('POST', 'HTTP POST'), ('PUT', 'FTP PUT'))
DATASET_CATEGORIES = (('observed', 'Observed datasets'), ('re-analysis', 'Re-analysis datasets'), ('CMIP5', 'CMIP5 Models'))
EXPERIMENT_DATASET_CATEGORIES = (('predictor', 'Predictor'), ('predictand', 'Predictand'))
FREQUENCIES = (('day', 'daily data'), ('month', 'monthly data'))


# Create your models here.

class Dataset(models.Model):

	category = models.CharField(max_length=20, choices=DATASET_CATEGORIES, default='', blank=True)
	short_name = models.CharField(max_length=50)
	description = models.TextField()
	source_url = models.URLField()


class Experiment(models.Model):

	short_name = models.CharField(max_length=50, default='')
	description = models.TextField()

	created_by = models.ForeignKey(Profile)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	datasets = models.ManyToManyField(Dataset, through='ExperimentDatasets')

class ExperimentDatasets(models.Model):

	experiment = models.ForeignKey(Experiment)
	dataset = models.ForeignKey(Dataset)
	category = models.CharField(max_length=20, choices=EXPERIMENT_DATASET_CATEGORIES, default='', blank=True)

class Model(models.Model):

	name = models.CharField(max_length=50, default="")
	contact = models.ForeignKey(Profile)
	description = models.TextField(default="", blank=True)

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

class Upload(models.Model):

	timestamp = models.DateTimeField(null=True)
	submission = models.ForeignKey(Submission)

	format = models.CharField(max_length=10, choices=FILE_FORMATS, default='txt')
	mode = models.CharField(max_length=10, choices=SUBMISSION_MODES, default='POST')
	path = models.CharField(max_length=500, default='', blank=True)
	filename = models.CharField(max_length=500, default='', blank=True)
