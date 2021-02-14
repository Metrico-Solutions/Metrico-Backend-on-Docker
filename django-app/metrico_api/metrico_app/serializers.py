from rest_framework import serializers
from .models import Metric


class MetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metric # this is the model that is being serialized
        fields = '__all__'
