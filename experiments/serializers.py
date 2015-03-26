from rest_framework import serializers
from experiments.models import Experiment, Dataset


class ExperimentSerializer(serializers.HyperlinkedModelSerializer):

	created_by = serializers.StringRelatedField()

	class Meta:
		model = Experiment
		fields = ('meta', 'short_name', 'description', 'created_by', 'created', 'modified', 'datasets')

class DatasetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dataset
        fields = ('short_name', 'description', 'category', 'source_url')

