from rest_framework.routers import DefaultRouter

from apps.partials import ProcessViewSet
from apps.partials.views import AdvantageViewSet, DoublesidedImageViewSet

router = DefaultRouter()
router.register(r'advantages', AdvantageViewSet, basename='advantages')
router.register(r'images', DoublesidedImageViewSet, basename='images')
router.register(r'process', ProcessViewSet, basename='process')
