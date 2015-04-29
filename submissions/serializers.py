from rest_framework import serializers

from profiles.models import Profile
from submissions.models import Model, Submission, Upload
from experiments.models import Experiment


class ModelSerializer(serializers.ModelSerializer):

	class Meta:
		model = Model
		fields = ('slug', 'title', 'contact', 'description')


class SubmissionSerializer(serializers.ModelSerializer):

	class Meta:
		model = Submission


class UploadSerializer(serializers.ModelSerializer):

	#submission = serializers.HyperlinkedRelatedField(queryset=Submission.objects.all(), view_name='submission-detail')

	class Meta:
		model = Upload
		fields = ('timestamp', 'submission', 'format', 'mode', 'uploaded')


