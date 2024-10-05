from rest_framework import serializers, viewsets

from .stock_product import StockProductSerializer
from ..models import StockSection
from apps.partials.views import DoublesidedImageSerializer


class StockSectionSerializer(serializers.ModelSerializer):
    products = StockProductSerializer(many=True, read_only=True)
    preview_image = DoublesidedImageSerializer(read_only=True)

    class Meta:
        model = StockSection
        fields = '__all__'


class StockSectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StockSection.objects.all()
    serializer_class = StockSectionSerializer
