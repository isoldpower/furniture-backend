from rest_framework import serializers, viewsets

from ..models import Process


class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = ['order', 'paragraph']


class ProcessViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer
