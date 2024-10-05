from rest_framework import viewsets, serializers, mixins

from ..models import PhoneCallRequest


class PhoneCallRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneCallRequest
        fields = '__all__'


class PhoneCallRequestViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = PhoneCallRequest.objects.all()
    serializer_class = PhoneCallRequestSerializer
