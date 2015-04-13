from rest_framework import serializers
from experiments.models import TimePeriod, MetaExperiment, Experiment, Dataset


class TimePeriodSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = TimePeriod
		fields = ('begin', 'end')


class DatasetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dataset
        fields = ('title', 'description', 'category', 'source_url')


class ExperimentSerializer(serializers.HyperlinkedModelSerializer):

	created_by = serializers.StringRelatedField()
	timeperiods = TimePeriodSerializer(many=True)
	datasets = DatasetSerializer(many=True)

	class Meta:
		model = Experiment
		fields = ('id', 'slug', 'title', 'meta', 'description', 'fullname', 'created_by', 'created', 'modified', 'timeperiods', 'datasets')


class MetaExperimentSerializer(serializers.HyperlinkedModelSerializer):

	created_by = serializers.StringRelatedField()
	experiments = ExperimentSerializer(many=True)

	class Meta:
		model = MetaExperiment
		fields = ('id', 'slug', 'title', 'description', 'fullname', 'created_by', 'created', 'modified', 'experiments')



