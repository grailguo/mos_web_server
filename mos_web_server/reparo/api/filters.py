from django_filters import rest_framework as filters

from mos_web_server.reparo.models import Device


# Create your api filters here.
class DeviceFilter(filters.FilterSet):
    class Meta:
        model = Device
        fields = ('name', 'model', 'sn',)

    pass
