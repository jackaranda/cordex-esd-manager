from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from django.contrib import messages

from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from profiles.models import Profile

from submissions.models import Model
from submissions.models import Submission

from experiments.models import Project
from experiments.models import MetaExperiment
from experiments.models import Experiment
from experiments.models import ExperimentTimePeriods
from experiments.models import ExperimentDatasets
from experiments.models import MetaCategory
from experiments.models import MetaTerm

from submissions.forms import SubmissionModelForm
from submissions.forms import SubmissionForm
from submissions.forms import UploadForm
from profiles.forms import ProfileForm


def index(request):

	try:
		user_profile = Profile.objects.get(user=request.user)
	except:
		user_profile = None

	return render(request, 'web/index.html', {'user_profile': user_profile})

def login_view(request):

	return render(request, 'web/login_methods.html')

@login_required
def user_profile(request):

	c = {}

	if 'edit' in request.GET:
		c['show_form'] = True
	else:
		c['show_form'] = False

	# First see if we already have a profile for this user
	try:
		profile = Profile.objects.get(user=request.user)
	except:
		profile = None

	# If we don't have a profile then we create a blank one
	if not profile:
		profile = Profile(user=request.user)
		profile.save()

	# If we have a profile, then we can fetch a list of models
	if profile:
		models = Model.objects.filter(contact=profile)
	else:
		models = []

	# Check if we have submitted POST data
	if request.method == "POST":
		
		profile_form = ProfileForm(request.POST)

		# If we can validate the form
		if profile_form.is_valid():

			# If we already have a profile then update it
			if profile:
				profile.institution = profile_form.cleaned_data['institution']
				profile.country = profile_form.cleaned_data['country']
				profile.save()

			# Otherwise we create a new profile and attach it to the logged in user
			else:
				profile = profile_form.save(commit=False)
				profile.user = request.user
				profile.save()
				messages.add_message(request, messages.INFO, 'Your profile has been saved')


		# If form has problems then we need to show it again
		else:
			c['show_form'] = True

	if profile:
		profile_form = ProfileForm(instance=profile)
	else:
		profile_form = ProfileForm()

	meta_category = MetaCategory.objects.filter(slug='esd')

	c['meta_terms'] = MetaTerm.objects.filter(category=meta_category)
	c['messages'] = messages.get_messages(request)
	c['profile_form'] = profile_form
	c['user_profile'] = profile
	c['user_models'] = models
	c['models_form'] = SubmissionModelForm()

	return render(request, 'web/profile.html', c)

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

	meta_experiments = MetaExperiment.objects.filter(project=project).order_by('id')

	return render(request, 'web/experiments.html', {'user_profile': user_profile, 'project':project, 'meta_experiments':meta_experiments})


def experiment_detail(request, project_slug, meta_slug, slug):

	try:
		user_profile = Profile.objects.get(user=request.user)
	except:
		user_profile = None

	project = get_object_or_404(Project, slug=project_slug)
	meta_experiment = get_object_or_404(MetaExperiment, project=project, slug=meta_slug)

	experiment = Experiment.objects.get(meta=meta_experiment, slug=slug)
	experiment_timeperiods = ExperimentTimePeriods.objects.filter(experiment=experiment)
	experiment_datasets = ExperimentDatasets.objects.filter(experiment=experiment)
	user_submissions = Submission.objects.filter(experiment=experiment, owner=user_profile)

	c = {}
	c['user_profile'] = user_profile
	c['project'] = project
	c['meta_experiment'] = meta_experiment
	c['experiment'] = experiment
	c['timeperiods'] = experiment_timeperiods
	c['datasets']  = experiment_datasets
	c['user_submissions'] = user_submissions


	return render(request, 'web/experiment_detail.html', c)


@login_required
def experiment_submissions(request, project_slug, meta_slug, slug):

	try:
		user_profile = Profile.objects.get(user=request.user)
	except:
		return HttpResponseRedirect(reverse('web-profile'))

#	user_models = Model.objects.filter(contact=user_profile)

	project = get_object_or_404(Project, slug=project_slug)
	meta_experiment = get_object_or_404(MetaExperiment, project=project, slug=meta_slug)
	experiment = Experiment.objects.get(meta=meta_experiment, slug=slug)

	user_submissions = Submission.objects.filter(experiment=experiment, owner=user_profile).order_by('experiment', '-version')


	c = {}
	c['user_profile'] = user_profile
#	c['user_models'] = user_models
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
			messages.info(request, "New submission created")

			#return HttpResponseRedirect('/submissions/{}/{}/{}'.format(project.slug, meta_experiment.slug, experiment.slug))
			return HttpResponseRedirect(reverse('web-experiment-submissions', args=(project.slug, meta_experiment.slug, experiment.slug,)))

		else:
			
			form.fields["model"].queryset = Model.objects.filter(contact=user_profile)
			c['form'] = form
			return render(request, 'web/submissions.html', c)

	submission_form = SubmissionForm()
	submission_form.fields["model"].queryset = Model.objects.filter(contact=user_profile)

	c['messages'] = messages.get_messages(request)
	c['form'] = submission_form
	c['upload_form'] = UploadForm()
	return render(request, 'web/submissions.html', c)


@login_required
def user_submissions(request):

	try:
		user_profile = Profile.objects.get(user=request.user)
	except:
		return HttpResponseRedirect(reverse('web-profile'))

	user_models = Model.objects.filter(contact=user_profile)

	user_submissions = Submission.objects.filter(owner=user_profile).order_by('experiment', '-version')

	c = {}
	c['user_profile'] = user_profile
	c['user_models'] = user_models
	c['user_submissions'] = user_submissions
	c['upload_form'] = UploadForm()

	return render(request, 'web/user_submissions.html', c)

@login_required
def admin_submissions(request):

	meta_experiments = MetaExperiment.objects.filter()
	models = Model.objects.filter().order_by('contact')
	submissions = Submission.objects.filter().order_by('owner', 'experiment', '-version')

	c = {}
	matrix = {}

	for meta_experiment in meta_experiments.all():
		sub_matrix = {}

		for experiment in meta_experiment.experiments.all():
			row = []

			for model in models.all():
				count = 0

				for submission in submissions.all():
					if submission.model == model and submission.experiment == experiment:
						count += 1

				row.append(count)

			sub_matrix[experiment] = row

		matrix[meta_experiment] = sub_matrix

	c['models'] = models
	c['matrix'] = matrix
	return render(request, 'web/admin_submissions.html', c)

def logout_view(request):

	logout(request)

	return HttpResponseRedirect(reverse('index'))



