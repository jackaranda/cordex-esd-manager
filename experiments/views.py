from django.shortcuts import render
from rest_framework import viewsets
from experiments.models import Dataset, Experiment
from experiments.serializers import DatasetSerializer, ExperimentSerializer


# Create your views here.
class DatasetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows datasets to be viewed or edited.
    """
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer

class ExperimentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows experiments to be viewed or edited.
    """
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer
