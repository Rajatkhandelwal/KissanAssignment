# Python imports
from rest_framework import serializers

# Engine imports
from weather.models import MaxTemperature, MinTemperature, Rainfall


class MetricsSerializer(serializers.ModelSerializer):
    year = serializers.ReadOnlyField()
    month = serializers.ReadOnlyField()


class MaxTempSerializer(MetricsSerializer):
    class Meta:
        model = MaxTemperature
        fields = ("value", "year", "month")


class MinTempSerializer(MetricsSerializer):
    class Meta:
        model = MinTemperature
        fields = ("value", "year", "month")


class RainfallSerializer(MetricsSerializer):
    class Meta:
        model = Rainfall
        fields = ("value", "year", "month")