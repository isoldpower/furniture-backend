from rest_framework import routers

from .views import PortfolioItemViewSet


router = routers.DefaultRouter()
router.register(r"", PortfolioItemViewSet, basename="portfolio")
