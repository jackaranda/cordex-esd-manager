from rest_framework import serializers
from submissions.models import Model, Submission, Upload
from experiments.models import Experiment


class ModelSerializer(serializers.HyperlinkedModelSerializer):

	contact = serializers.StringRelatedField()

	class Meta:
		model = Model
		fields = ('slug', 'title', 'contact', 'description')

class SubmissionSerializer(serializers.HyperlinkedModelSerializer):

	queryset = Submission.objects.all()
	owner = serializers.StringRelatedField()
	model = serializers.HyperlinkedRelatedField(queryset=Model.objects.all(), view_name='model-detail')
	model_name = serializers.StringRelatedField(read_only=True, source='model.title')
	experiment = serializers.HyperlinkedRelatedField(queryset=Experiment.objects.filter(meta=False), view_name='experiment-detail')
	experiment_name = serializers.StringRelatedField(read_only=True, source='experiment.title')
	uploads = serializers.StringRelatedField(many=True, read_only=True, source='timestamp')

	class Meta:
		model = Submission
		fields = ('owner', 'model', 'model_name', 'experiment', 'experiment_name', 'version', 'uploads')

class UploadSerializer(serializers.HyperlinkedModelSerializer):

	submission = serializers.HyperlinkedRelatedField(queryset=Submission.objects.all(), view_name='submission-detail')

	class Meta:
		model = Upload
		fields = ('timestamp', 'submission', 'format', 'mode', 'uploaded')


