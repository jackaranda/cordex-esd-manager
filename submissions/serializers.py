from rest_framework import serializers
from submissions.models import Model, Submission, Upload


class ModelSerializer(serializers.HyperlinkedModelSerializer):

	contact = serializers.StringRelatedField()

	class Meta:
		model = Model
		fields = ('slug', 'title', 'contact', 'description')

class SubmissionSerializer(serializers.HyperlinkedModelSerializer):

	owner = serializers.StringRelatedField()
	model = serializers.HyperlinkedRelatedField(read_only=True, view_name='model-detail')
	experiment = serializers.HyperlinkedRelatedField(read_only=True, view_name='experiment-detail')

	class Meta:
		model = Submission
		fields = ('owner', 'model', 'experiment', 'version')

#class UploadSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = Dataset
#        fields = ('title', 'description', 'category', 'source_url')

