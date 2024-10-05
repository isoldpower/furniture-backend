from rest_framework import routers

from .views import SettingsViewSet

router = routers.DefaultRouter()
router.register(r"", SettingsViewSet)
