from rest_framework import serializers

from ..models import MaterialAdvantage, FirmAdvantage


class FirmAdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirmAdvantage
        fields = '__all__'


class MaterialAdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialAdvantage
        fields = '__all__'
