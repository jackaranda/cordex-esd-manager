from django.db import models
from profiles.models import Profile


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


