from rest_framework import serializers, viewsets

from .product_material import ProductMaterialSerializer
from ..models import StockProduct
from apps.partials.views import DoublesidedImageSerializer


class StockProductSerializer(serializers.ModelSerializer):
    materials = ProductMaterialSerializer(many=True, read_only=True)
    images = DoublesidedImageSerializer(many=True, read_only=True)

    class Meta:
        model = StockProduct
        fields = '__all__'


class StockProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StockProduct.objects.all()
    serializer_class = StockProductSerializer
