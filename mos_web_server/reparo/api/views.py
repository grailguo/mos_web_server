from rest_framework import viewsets, permissions

from mos_web_server.reparo.api.filters import DeviceFilter
from mos_web_server.reparo.api.serializers import DeviceSerializer
from mos_web_server.reparo.models import Device


# Create your api views here.
class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all().order_by('id')
    serializer_class = DeviceSerializer
    filterset_class = DeviceFilter
    search_fields = ['name', 'model', 'sn']
    permission_classes = [permissions.IsAuthenticated]
    pass
