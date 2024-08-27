from rest_framework import serializers, viewsets

from ..models import DoublesidedImage


class DoublesidedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoublesidedImage
        fields = '__all__'


class DoublesidedImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DoublesidedImage.objects.all()
    serializer_class = DoublesidedImageSerializer

