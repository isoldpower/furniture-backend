from rest_framework import serializers, viewsets

from . import DoublesidedImageSerializer
from ..models import Process


class ProcessSerializer(serializers.ModelSerializer):
    image = DoublesidedImageSerializer(read_only=True, many=False)

    class Meta:
        model = Process
        fields = ['order', 'paragraph', 'image']


class ProcessViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer
