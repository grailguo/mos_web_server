from rest_framework import serializers

from reparo.models import Device


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    activated = serializers.BooleanField(default=True, initial=True)

    class Meta:
        model = Device
        fields = '__all__'

    pass
