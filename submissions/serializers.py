from rest_framework import serializers

from profiles.models import Profile
from submissions.models import ModelMeta, Model, Submission, Upload
from experiments.models import Experiment, MetaValue


class ModelMetaSerializer(serializers.ModelSerializer):
	entry = serializers.PrimaryKeyRelatedField(read_only=False, queryset=MetaValue.objects.all())

	class Meta:
		model = ModelMeta
		fields = ('entry',)

class ModelSerializer(serializers.ModelSerializer):

	metadata = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=MetaValue.objects.all())

	class Meta:
		model = Model
		fields = ('slug', 'title', 'description', 'contact', 'metadata')


class SubmissionSerializer(serializers.ModelSerializer):

	class Meta:
		model = Submission


class UploadSerializer(serializers.ModelSerializer):

	#submission = serializers.HyperlinkedRelatedField(queryset=Submission.objects.all(), view_name='submission-detail')

	class Meta:
		model = Upload
		fields = ('timestamp', 'submission', 'format', 'mode', 'uploaded')


