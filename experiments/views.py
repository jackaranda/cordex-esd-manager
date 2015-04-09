from django.shortcuts import render
from rest_framework import viewsets
from experiments.models import TimePeriod, Dataset, MetaExperiment, Experiment
from experiments.serializers import TimePeriodSerializer, DatasetSerializer, MetaExperimentSerializer, ExperimentSerializer


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


class MetaExperimentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows meta experiments to be viewed or edited.
    """
    queryset = MetaExperiment.objects.all()
    serializer_class = MetaExperimentSerializer


class ExperimentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows experiments to be viewed or edited.
    """
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer
