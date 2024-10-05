from rest_framework import serializers, viewsets

from ..models import MaterialAdvantage, FirmAdvantage
from ..models.abstracts import AbstractAdvantage


class AdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbstractAdvantage
        fields = ['id', 'title', 'paragraph']


class AdvantageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AbstractAdvantage.objects.all()
    serializer_class = AdvantageSerializer

    def get_queryset(self):
        queryset = AbstractAdvantage.objects.all()
        purpose = self.request.query_params.get('purpose')
        if purpose is not None:
            queryset = queryset.filter(purpose=purpose)
        return queryset


class FirmAdvantageSerializer(AdvantageSerializer):
    class Meta:
        model = FirmAdvantage
        fields = AdvantageSerializer.Meta.fields


class MaterialAdvantageSerializer(AdvantageSerializer):
    class Meta:
        model = MaterialAdvantage
        fields = AdvantageSerializer.Meta.fields
