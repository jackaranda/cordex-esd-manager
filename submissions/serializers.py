from rest_framework import serializers

from profiles.models import Profile
from submissions.models import Model, Submission, Upload
from experiments.models import Experiment


class ModelSerializer(serializers.HyperlinkedModelSerializer):

	contact = serializers.StringRelatedField()

	class Meta:
		model = Model
		fields = ('slug', 'title', 'contact', 'description')

#class SubmissionSerializer(serializers.HyperlinkedModelSerializer):

#	queryset = Submission.objects.all()
	#owner = serializers.StringRelatedField()
#	owner = serializers.PrimaryKeyRelatedField(read_only=True)
#	model = serializers.HyperlinkedRelatedField(queryset=Model.objects.all(), view_name='model-detail')
	#model_name = serializers.StringRelatedField(read_only=True, source='model.title')
#	experiment = serializers.HyperlinkedRelatedField(queryset=Experiment.objects.all(), view_name='experiment-detail')
	#experiment_name = serializers.StringRelatedField(read_only=True, source='experiment.title')
	#uploads = serializers.StringRelatedField(many=True, read_only=True, source='timestamp')

#	class Meta:
#		model = Submission
#		fields = ('owner', 'model', 'experiment', 'version', 'uploads')

class SubmissionSerializer(serializers.ModelSerializer):

	class Meta:
		model = Submission


class UploadSerializer(serializers.HyperlinkedModelSerializer):

	submission = serializers.HyperlinkedRelatedField(queryset=Submission.objects.all(), view_name='submission-detail')

	class Meta:
		model = Upload
		fields = ('timestamp', 'submission', 'format', 'mode', 'uploaded')


