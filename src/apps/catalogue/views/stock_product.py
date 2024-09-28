from rest_framework import serializers, viewsets

from .product_material import ProductMaterialSerializer
from ..models import StockProduct
from apps.partials.views import DoublesidedImageSerializer
from ..services.filter_important import get_important_items


class StockProductSerializer(serializers.ModelSerializer):
    materials = ProductMaterialSerializer(many=True, read_only=True)
    images = DoublesidedImageSerializer(many=True, read_only=True)

    class Meta:
        model = StockProduct
        fields = '__all__'


class StockProductViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StockProductSerializer

    def get_queryset(self):
        queryset = StockProduct.objects.all()
        return get_important_items(self, queryset)
