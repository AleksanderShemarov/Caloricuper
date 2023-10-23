from rest_framework import serializers
from .models import WeightIndexLevel


class WeightIndexLevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = WeightIndexLevel
        fields = '__all__'
