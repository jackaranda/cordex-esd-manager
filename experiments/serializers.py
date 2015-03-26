from rest_framework import serializers
from experiments.models import Experiment, Dataset


class ExperimentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Experiment
        fields = ('short_name', 'description', 'created_by', 'created', 'modified', 'datasets')

class DatasetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dataset
        fields = ('short_name', 'description', 'category', 'source_url')

