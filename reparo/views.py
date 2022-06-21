from rest_framework import viewsets, permissions

from reparo.filters import DeviceFilter
from reparo.models import Device
from reparo.serializers import DeviceSerializer


# Create your views here.
class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all().order_by('id')
    serializer_class = DeviceSerializer
    filterset_class = DeviceFilter
    search_fields = ['name', 'model', 'sn']
    permission_classes = [permissions.IsAuthenticated]
    pass
