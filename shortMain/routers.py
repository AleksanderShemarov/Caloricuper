from rest_framework import routers
from .viewsets import WeightIndexLevelViewSet


router = routers.SimpleRouter()
router.register(r'main', WeightIndexLevelViewSet, basename='short-main')
