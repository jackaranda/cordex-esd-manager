from django.shortcuts import render
from rest_framework import viewsets
from submissions.models import Dataset
from submissions.serializers import DatasetSerializer


# Create your views here.
class DatasetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows datasets to be viewed or edited.
    """
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer
