from .views import ProductMaterialViewSet, StockProductViewSet, StockSectionViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'materials', ProductMaterialViewSet, basename='materials')
router.register(r'products', StockProductViewSet, basename='products')
router.register(r'sections', StockSectionViewSet, basename='sections')
