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


class FirmAdvantageSerializer(AdvantageSerializer):
    class Meta:
        model = FirmAdvantage
        fields = '__all__'


class MaterialAdvantageSerializer(AdvantageSerializer):
    class Meta:
        model = MaterialAdvantage
        fields = '__all__'
