from rest_framework import routers

from .views import PhoneCallRequestViewSet


router = routers.DefaultRouter()
router.register(r'phone-call', PhoneCallRequestViewSet, basename='phone-call')
