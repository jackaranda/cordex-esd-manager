from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from profiles.models import Profile

from submissions.models import Model
from submissions.models import Submission

from experiments.models import Project
from experiments.models import MetaExperiment
from experiments.models import Experiment
from experiments.models import ExperimentTimePeriods
from experiments.models import ExperimentDatasets

from submissions.forms import SubmissionForm
from submissions.forms import UploadForm

# Create your views here.

def index(request):

	try:
		user_profile = Profile.objects.get(user=request.user)
	except:
		user_profile = None

	return render(request, 'web/index.html', {'user_profile': user_profile})



def projects(request):

	try:
		user_profile = Profile.objects.get(user=request.user)
	except:
		user_profile = None

	return render(request, 'web/projects.html',  {'user_profile': user_profile})



def experiments(request, slug):

	try:
		user_profile = Profile.objects.get(user=request.user)
	except:
		user_profile = None

	project = get_object_or_404(Project, slug=slug)

	meta_experiments = MetaExperiment.objects.filter(project=project)

	return render(request, 'web/experiments.html', {'user_profile': user_profile, 'project':project, 'meta_experiments':meta_experiments})


def experiment_detail(request, project_slug, meta_slug, slug):

	try:
		user_profile = Profile.objects.get(user=request.user)
	except:
		user_profile = None

	user_models = Model.objects.filter(contact=user_profile)

	project = get_object_or_404(Project, slug=project_slug)
	meta_experiment = get_object_or_404(MetaExperiment, project=project, slug=meta_slug)

	experiment = Experiment.objects.get(meta=meta_experiment, slug=slug)
	experiment_timeperiods = ExperimentTimePeriods.objects.filter(experiment=experiment)
	experiment_datasets = ExperimentDatasets.objects.filter(experiment=experiment)

	c = {}
	c['user_profile'] = user_profile
	c['user_models'] = user_models
	c['project'] = project
	c['meta_experiment'] = meta_experiment
	c['experiment'] = experiment
	c['timeperiods'] = experiment_timeperiods
	c['datasets']  = experiment_datasets


	return render(request, 'web/experiment_detail.html', c)


def submissions(request, project_slug, meta_slug, slug):

	try:
		user_profile = Profile.objects.get(user=request.user)
	except:
		user_profile = None

	user_models = Model.objects.filter(contact=user_profile)
	user_submissions = Submission.objects.all().order_by('experiment', '-version')

	project = get_object_or_404(Project, slug=project_slug)
	meta_experiment = get_object_or_404(MetaExperiment, project=project, slug=meta_slug)

	experiment = Experiment.objects.get(meta=meta_experiment, slug=slug)

	c = {}
	c['user_profile'] = user_profile
	c['user_models'] = user_models
	c['user_submissions'] = user_submissions
	c['project'] = project
	c['meta_experiment'] = meta_experiment
	c['experiment'] = experiment


	if request.method == 'POST':
		
		form = SubmissionForm(request.POST)

		if form.is_valid():

			clean = form.cleaned_data
			# Check for previous versions
			previous = Submission.objects.filter(model=clean['model'], experiment=clean['experiment'], owner=clean['owner']).order_by('-version')

			if previous:
				version = previous[0].version + 1
			else:
				version = 1

			new_submission = form.save(commit=False)
			new_submission.version = version
			new_submission.save()

			return HttpResponseRedirect('/submissions/{}/{}/{}'.format(project.slug, meta_experiment.slug, experiment.slug))

		else:
			
			c['form'] = form
			return render(request, 'web/submissions.html', c)


	c['form'] = SubmissionForm({'model':user_models[0]})
	c['upload_form'] = UploadForm()
	return render(request, 'web/submissions.html', c)

def test(request):
	return render(request, 'web/test.html')
