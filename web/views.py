from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def experiments(request):
	return render(request, 'web/experiments.html')

def submissions(request):
	return render(request, 'web/submissions.html')
