from rest_framework import serializers

from profiles.models import Profile
from submissions.models import ModelMeta, Model, Submission, Upload
from experiments.models import Experiment, MetaTerm, MetaControlledValue


class ModelMetaSerializer(serializers.ModelSerializer):
	
	model = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Model.objects.all())
	term = serializers.PrimaryKeyRelatedField(read_only=False, queryset=MetaTerm.objects.all())

	class Meta:
		model = ModelMeta
		fields = ('model', 'term','value')


class ModelSerializer(serializers.ModelSerializer):

	class Meta:
		model = Model
		fields = ('id', 'slug', 'title', 'description', 'contact')


class SubmissionSerializer(serializers.ModelSerializer):

	class Meta:
		model = Submission


class UploadSerializer(serializers.ModelSerializer):

	#submission = serializers.HyperlinkedRelatedField(queryset=Submission.objects.all(), view_name='submission-detail')

	class Meta:
		model = Upload
		fields = ('timestamp', 'submission', 'format', 'mode', 'uploaded')


