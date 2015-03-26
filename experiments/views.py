from django.shortcuts import render
from rest_framework import viewsets
from experiments.models import TimePeriod, Dataset, Experiment
from experiments.serializers import TimePeriodSerializer, DatasetSerializer, ExperimentSerializer


# Create your views here.
class TimePeriodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows timeperiods to be viewed or edited
    """
    queryset = TimePeriod.objects.all()
    serializer_class = TimePeriodSerializer

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
