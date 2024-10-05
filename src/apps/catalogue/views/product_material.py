from rest_framework import serializers, viewsets

from ..models import ProductMaterial
from apps.partials.views import MaterialAdvantageSerializer, DoublesidedImageSerializer
from ..services.filter_important import get_important_items


class ProductMaterialSerializer(serializers.ModelSerializer):
    advantages = MaterialAdvantageSerializer(many=True, read_only=True)
    image = DoublesidedImageSerializer(read_only=True)

    class Meta:
        model = ProductMaterial
        fields = "__all__"


class ProductMaterialViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductMaterialSerializer

    def get_queryset(self):
        queryset = ProductMaterial.objects.all()
        return get_important_items(self, queryset)
