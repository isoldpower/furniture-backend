from rest_framework import serializers, viewsets

from ..models import ProductMaterial
from apps.partials.views import MaterialAdvantageSerializer, DoublesidedImageSerializer


class ProductMaterialSerializer(serializers.ModelSerializer):
    advantages = MaterialAdvantageSerializer(many=True, read_only=True)
    image = DoublesidedImageSerializer(read_only=True)

    class Meta:
        model = ProductMaterial
        fields = "__all__"


class ProductMaterialViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProductMaterial.objects.all()
    serializer_class = ProductMaterialSerializer
