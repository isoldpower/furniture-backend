from rest_framework import viewsets, serializers

from apps.partials.views import DoublesidedImageSerializer
from ..models import PortfolioItem


class PortfolioItemSerializer(serializers.ModelSerializer):
    image = DoublesidedImageSerializer()

    class Meta:
        model = PortfolioItem
        fields = '__all__'


class PortfolioItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PortfolioItem.objects.all()
    serializer_class = PortfolioItemSerializer
