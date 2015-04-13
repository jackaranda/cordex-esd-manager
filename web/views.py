from django.shortcuts import render
from django.http import HttpResponse
from profiles.models import Profile
from submissions.models import Model
# Create your views here.

def index(request):

	return render(request, 'web/index.html')

def experiments(request):

	user_profile = Profile.objects.get(user=request.user)
	user_models = Model.objects.filter(contact=user_profile)

	return render(request, 'web/experiments.html', {'user_profile': user_profile, 'user_models': user_models})

def submissions(request):
	return render(request, 'web/submissions.html')

def test(request):
	return render(request, 'web/test.html')
