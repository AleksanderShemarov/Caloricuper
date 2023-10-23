from rest_framework import viewsets
from .models import WeightIndexLevel
from .serializers import WeightIndexLevelSerializer


class WeightIndexLevelViewSet(viewsets.ModelViewSet):
    serializer_class = WeightIndexLevelSerializer

    def get_queryset(self):
        return WeightIndexLevel.objects.all()
