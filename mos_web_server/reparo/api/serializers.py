from rest_framework import serializers

from mos_web_server.reparo.models import Device


# Create your api serializers here.
# Serializers define the API representation.
class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    activated = serializers.BooleanField(default=True, initial=True)

    class Meta:
        model = Device
        fields = '__all__'

    pass
