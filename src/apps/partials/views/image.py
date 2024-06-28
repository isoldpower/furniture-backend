from rest_framework import serializers

from ..models import DoublesidedImage


class DoublesidedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoublesidedImage
        fields = '__all__'
