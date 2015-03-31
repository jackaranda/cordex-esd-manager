from django.shortcuts import render
from rest_framework import viewsets
from submissions.serializers import ModelSerializer, SubmissionSerializer, UploadSerializer
from submissions.models import Model, Submission, Upload

from rest_framework import permissions
from submissions.permissions import IsOwnerOrReadOnly

class ModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows models to be viewed or edited
    """
    queryset = Model.objects.all()
    serializer_class = ModelSerializer


class SubmissionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows submissions to be viewed or edited
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

class UploadViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows upload to be viewed or edited
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer

