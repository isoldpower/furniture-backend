from rest_framework import serializers, viewsets, mixins

from ..models import SectionedSettings


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionedSettings
        fields = ['key', 'value']


class SettingsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = SettingsSerializer
    queryset = SectionedSettings.objects.all()
