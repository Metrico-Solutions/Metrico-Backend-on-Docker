from django.db import models


class Metric(models.Model):
    metric_name = models.CharField(max_length=100)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.metric_name
