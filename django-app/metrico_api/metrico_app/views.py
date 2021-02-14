from rest_framework import viewsets
from .serializers import MetricSerializer
from.models import Metric


class MetricViewSet(viewsets.ModelViewSet):
    serializer_class = MetricSerializer
    queryset = Metric.objects.all()
