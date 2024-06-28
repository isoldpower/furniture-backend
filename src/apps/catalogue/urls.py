from .views import ProductMaterialViewSet, StockProductViewSet, StockSectionViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'materials', ProductMaterialViewSet)
router.register(r'products', StockProductViewSet)
router.register(r'sections', StockSectionViewSet)
