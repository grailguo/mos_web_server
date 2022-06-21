from django_filters import rest_framework as filters

from reparo.models import Device


class DeviceFilter(filters.FilterSet):
    class Meta:
        model = Device
        fields = ('name', 'model', 'sn',)

    pass
