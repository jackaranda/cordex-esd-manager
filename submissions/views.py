import os

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import views
from rest_framework import parsers
from rest_framework import mixins
from submissions.serializers import ModelSerializer, SubmissionSerializer, UploadSerializer
from submissions.models import Model, Submission, Upload
from profiles.models import Profile

from rest_framework import permissions
from submissions.permissions import UploadsIsOwnerOrReadOnly

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
    permission_classes = [permissions.IsAuthenticated]
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

    def get_queryset(self):
        try:
            user_profile = Profile.objects.get(user=self.request.user)
        except:
            return None

        return Submission.objects.filter(owner=user_profile)

#class UploadViewSet(viewsets.ModelViewSet):
#    """
#    API endpoint that allows upload to be viewed or edited
#    """
#    permission_classes = [IsOwnerOrReadOnly]
#    queryset = Upload.objects.all()
#    serializer_class = UploadSerializer

class UploadView(viewsets.ModelViewSet):

    permission_classes = [UploadsIsOwnerOrReadOnly]
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer
    parser_classes = (parsers.FormParser, parsers.MultiPartParser)

#    def post(self, request, filename):

#        upload_file = request.data['file']

#        with open('test', 'w') as target:
#            for chunk in upload_file.chunks():
#                target.write(chunk)

    def perform_destroy(self, instance):

        # Delete the actual file
        if instance.uploaded:
            if os.path.isfile(instance.uploaded.path):
                os.remove(instance.uploaded.path)

        # Delete the database
        instance.delete()



