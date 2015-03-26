from rest_framework import serializers
from submissions.models import Dataset


class DatasetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dataset
        fields = ('url', 'category', 'short_name', 'description', 'source_url')

