from rest_framework import serializers
from experiments.models import TimePeriod, Experiment, Dataset


class TimePeriodSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = TimePeriod
		fields = ('begin', 'end')

class ExperimentSerializer(serializers.HyperlinkedModelSerializer):

	created_by = serializers.StringRelatedField()

	class Meta:
		model = Experiment
		fields = ('meta', 'parent', 'children', 'title', 'description', 'fullname', 'created_by', 'created', 'modified', 'timeperiods', 'datasets')

class DatasetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dataset
        fields = ('title', 'description', 'category', 'source_url')

