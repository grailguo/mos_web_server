from rest_framework import viewsets, permissions

from mos_web_server.accio.api.serializers import CompoundTagSerializer, CompoundSerializer, ExperimentSerializer, \
    SpectrumTagSerializer, SpectrumSerializer, QuantMethodSerializer, CartridgeSerializer
from mos_web_server.accio.models import CompoundTag, Compound, Experiment, SpectrumTag, Spectrum, QuantMethod, Cartridge


# Create your views here.
class CompoundTagViewSet(viewsets.ModelViewSet):
    queryset = CompoundTag.objects.all().order_by('id')
    serializer_class = CompoundTagSerializer
    permission_classes = [permissions.IsAuthenticated]
    pass


class CompoundViewSet(viewsets.ModelViewSet):
    queryset = Compound.objects.all().order_by('id')
    serializer_class = CompoundSerializer
    permission_classes = [permissions.IsAuthenticated]
    pass


class ExperimentViewSet(viewsets.ModelViewSet):
    queryset = Experiment.objects.all().order_by('id')
    serializer_class = ExperimentSerializer
    permission_classes = [permissions.IsAuthenticated]
    pass


class SpectrumTagViewSet(viewsets.ModelViewSet):
    queryset = SpectrumTag.objects.all().order_by('id')
    serializer_class = SpectrumTagSerializer
    permission_classes = [permissions.IsAuthenticated]
    pass


class SpectrumViewSet(viewsets.ModelViewSet):
    queryset = Spectrum.objects.all().order_by('id')
    serializer_class = SpectrumSerializer
    permission_classes = [permissions.IsAuthenticated]
    pass


class QuantMethodViewSet(viewsets.ModelViewSet):
    queryset = QuantMethod.objects.all().order_by('id')
    serializer_class = QuantMethodSerializer
    permission_classes = [permissions.IsAuthenticated]
    pass


class CartridgeViewSet(viewsets.ModelViewSet):
    queryset = Cartridge.objects.all().order_by('id')
    serializer_class = CartridgeSerializer
    permission_classes = [permissions.IsAuthenticated]
    pass
