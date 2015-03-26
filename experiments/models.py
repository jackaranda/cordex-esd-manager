from django.db import models
from profiles.models import Profile


DATASET_CATEGORIES = (('observed', 'Observed datasets'), ('re-analysis', 'Re-analysis datasets'), ('CMIP5', 'CMIP5 Models'))
EXPERIMENT_DATASET_CATEGORIES = (('predictor', 'Predictor'), ('predictand', 'Predictand'))
FREQUENCIES = (('day', 'daily data'), ('month', 'monthly data'))


class Project(models.Model):

	short_name = models.CharField(max_length=50)
	description = models.TextField()
	url = models.URLField(default="")

	created_by = models.ForeignKey(Profile, null=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.short_name

class Dataset(models.Model):

	short_name = models.CharField(max_length=50)
	description = models.TextField()
	category = models.CharField(max_length=20, choices=DATASET_CATEGORIES, default='', blank=True)
	source_url = models.URLField()

	def __unicode__(self):
		return self.short_name


class Experiment(models.Model):

	short_name = models.CharField(max_length=50, default='')
	description = models.TextField()
	meta = models.BooleanField(default=False)

	project = models.ForeignKey(Project, null=True)

	created_by = models.ForeignKey(Profile)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	datasets = models.ManyToManyField(Dataset, through='ExperimentDatasets')

	def __unicode__(self):
		return self.short_name


class ExperimentDatasets(models.Model):

	experiment = models.ForeignKey(Experiment)
	dataset = models.ForeignKey(Dataset)
	category = models.CharField(max_length=20, choices=EXPERIMENT_DATASET_CATEGORIES, default='', blank=True)

	def __unicode__(self):
		return "{} ({})".format(self.dataset, self.category)


