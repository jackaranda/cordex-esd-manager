from django.db import models
from profiles.models import Profile

import datetime


DATASET_CATEGORIES = (('observed', 'Observed datasets'), ('re-analysis', 'Re-analysis datasets'), ('CMIP5', 'CMIP5 Models'))
EXPERIMENT_DATASET_CATEGORIES = (('predictor', 'Predictor'), ('predictand', 'Predictand'))
EXPERIMENT_VARIABLE_CATEGORIES = (('forcing', 'Forcing'), ('output', 'Output'))
TIMEPERIOD_CATEGORIES = (('calibration', 'Calibration period'), ('validation', 'Validation period'))
FREQUENCIES = (('day', 'daily data'), ('month', 'monthly data'))
META_DEPENDENCY_CATEGORIES = (('Equal', 'equal'),)


class TimePeriod(models.Model):

	short_name = models.CharField(max_length=50, default="", blank=True)
	begin = models.DateTimeField(default=datetime.datetime(1900,1,1))
	end = models.DateTimeField(default=datetime.datetime(1999,12,31))

	#exclude = models.ManyToManyField('TimePeriod')

	def __unicode__(self):
		return "{} - {}".format(self.begin, self.end)


class Variable(models.Model):

	short_name = models.SlugField(max_length=50, default="", blank=False, unique=True)
	long_name = models.CharField(max_length=100, default="", blank=True)
	standard_name = models.CharField(max_length=100, default="", blank=True)
	units = models.CharField(max_length=15)

	comments = models.TextField(blank=True, default="")

	def __unicode__(self):
		return self.standard_name


class Project(models.Model):

	slug = models.SlugField(max_length=50)
	title = models.CharField(max_length=50, default='')
	description = models.TextField()
	url = models.URLField(default="")

	created_by = models.ForeignKey(Profile, null=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.title

class Dataset(models.Model):

	slug = models.SlugField(max_length=50)
	title = models.CharField(max_length=50, default='')
	description = models.TextField()
	category = models.CharField(max_length=20, choices=DATASET_CATEGORIES, default='', blank=True)
	source_url = models.URLField()

	def __unicode__(self):
		return self.title

class MetaExperiment(models.Model):

	slug = models.SlugField(max_length=50)
	title = models.CharField(max_length=50, default='')
	description = models.TextField()

	project = models.ForeignKey(Project, null=True)

	created_by = models.ForeignKey(Profile)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	metadata_category = models.ForeignKey('MetaCategory', null=True, blank=True)

	def fullname(self):
		return "{} | {}".format(self.project, self.title)

	def __unicode__(self):
		return self.title


class Experiment(models.Model):

	slug = models.SlugField(max_length=50)
	title = models.CharField(max_length=50, default='')
	description = models.TextField()

	#project = models.ForeignKey(Project, null=True)

	meta = models.ForeignKey('MetaExperiment', null=True, blank=True, related_name='experiments')

	created_by = models.ForeignKey(Profile)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	datasets = models.ManyToManyField(Dataset, through='ExperimentDatasets')
	timeperiods = models.ManyToManyField(TimePeriod, through='ExperimentTimePeriods')
	variables = models.ManyToManyField(Variable, through='ExperimentVariables')


	def fullname(self):
		return "{}".format(self.title)


	def __unicode__(self):
		return self.title


class ExperimentDatasets(models.Model):

	experiment = models.ForeignKey(Experiment)
	dataset = models.ForeignKey(Dataset)
	category = models.CharField(max_length=20, choices=EXPERIMENT_DATASET_CATEGORIES, default='', blank=True)

	def __unicode__(self):
		return "{} - {} ({})".format(self.experiment, self.dataset, self.category)


class ExperimentVariables(models.Model):

	experiment = models.ForeignKey(Experiment)
	variable = models.ForeignKey(Variable)
	category = models.CharField(max_length=20, choices=EXPERIMENT_VARIABLE_CATEGORIES, default='', blank=True)

	def __unicode__(self):
		return "{} - {} ({})".format(self.experiment, self.variable, self.category)


class ExperimentTimePeriods(models.Model):

	experiment = models.ForeignKey(Experiment)
	timeperiod = models.ForeignKey(TimePeriod)
	category = models.CharField(max_length=20, choices=TIMEPERIOD_CATEGORIES, default='', blank=True)

	def __unicode__(self):
		return "{} - {} ({})".format(self.experiment, self.timeperiod, self.category)


class MetaCategory(models.Model):

	slug = models.SlugField()
	description = models.TextField(default="")

	def __unicode__(self):
		return self.slug

class MetaTerm(models.Model):

	category = models.ForeignKey(MetaCategory)
	name = models.SlugField()
	long_name = models.CharField(max_length=100, default="")
	help_text = models.TextField(default="", blank=True)
	multiple = models.BooleanField(default=False)
#	depends_on = models.ForeignKey('ModelMetaDependencies') 

	def __unicode__(self):
		return "{}:{}".format(self.category,self.name)

class MetaDependency(models.Model):

	depends_on = models.ForeignKey(MetaTerm, related_name='depended_on')
	category = models.TextField(choices=META_DEPENDENCY_CATEGORIES)
	depends_value = models.ForeignKey('MetaValue')

class MetaValue(models.Model):

	term = models.ForeignKey(MetaTerm, related_name='values')
	value = models.CharField(max_length=100)

	def __unicode__(self):
		return "{}:{}".format(self.term, self.value)