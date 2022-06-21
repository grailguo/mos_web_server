
from rest_framework import viewsets
from tyadmin_api.custom import XadminViewSet
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from erecto.models import MethodType, AnalysisType, Matrix, Source, Eluent, Unit, ConcUnit
from reparo.models import Device
from accio.models import CompoundCodeCounter, CompoundTag, Compound, Experiment, SpectrumTag, Spectrum, QuantMethodCodeCounter, QuantMethod, Cartridge

from tyadmin_api.auto_serializers import PermissionListSerializer, GroupListSerializer, ContentTypeListSerializer, MethodTypeListSerializer, AnalysisTypeListSerializer, MatrixListSerializer, SourceListSerializer, EluentListSerializer, UnitListSerializer, ConcUnitListSerializer, DeviceListSerializer, CompoundCodeCounterListSerializer, CompoundTagListSerializer, CompoundListSerializer, ExperimentListSerializer, SpectrumTagListSerializer, SpectrumListSerializer, QuantMethodCodeCounterListSerializer, QuantMethodListSerializer, CartridgeListSerializer
from tyadmin_api.auto_serializers import PermissionCreateUpdateSerializer, GroupCreateUpdateSerializer, ContentTypeCreateUpdateSerializer, MethodTypeCreateUpdateSerializer, AnalysisTypeCreateUpdateSerializer, MatrixCreateUpdateSerializer, SourceCreateUpdateSerializer, EluentCreateUpdateSerializer, UnitCreateUpdateSerializer, ConcUnitCreateUpdateSerializer, DeviceCreateUpdateSerializer, CompoundCodeCounterCreateUpdateSerializer, CompoundTagCreateUpdateSerializer, CompoundCreateUpdateSerializer, ExperimentCreateUpdateSerializer, SpectrumTagCreateUpdateSerializer, SpectrumCreateUpdateSerializer, QuantMethodCodeCounterCreateUpdateSerializer, QuantMethodCreateUpdateSerializer, CartridgeCreateUpdateSerializer
from tyadmin_api.auto_filters import PermissionFilter, GroupFilter, ContentTypeFilter, MethodTypeFilter, AnalysisTypeFilter, MatrixFilter, SourceFilter, EluentFilter, UnitFilter, ConcUnitFilter, DeviceFilter, CompoundCodeCounterFilter, CompoundTagFilter, CompoundFilter, ExperimentFilter, SpectrumTagFilter, SpectrumFilter, QuantMethodCodeCounterFilter, QuantMethodFilter, CartridgeFilter

    
class PermissionViewSet(XadminViewSet):
    serializer_class = PermissionListSerializer
    queryset = Permission.objects.all().order_by('-pk')
    filter_class = PermissionFilter
    search_fields = ["name","codename"]

    def get_serializer_class(self):
        if self.action == "list":
            return PermissionListSerializer
        else:
            return PermissionCreateUpdateSerializer

    
class GroupViewSet(XadminViewSet):
    serializer_class = GroupListSerializer
    queryset = Group.objects.all().order_by('-pk')
    filter_class = GroupFilter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return GroupListSerializer
        else:
            return GroupCreateUpdateSerializer

    
class ContentTypeViewSet(XadminViewSet):
    serializer_class = ContentTypeListSerializer
    queryset = ContentType.objects.all().order_by('-pk')
    filter_class = ContentTypeFilter
    search_fields = ["app_label","model"]

    def get_serializer_class(self):
        if self.action == "list":
            return ContentTypeListSerializer
        else:
            return ContentTypeCreateUpdateSerializer

    
class MethodTypeViewSet(XadminViewSet):
    serializer_class = MethodTypeListSerializer
    queryset = MethodType.objects.all().order_by('-pk')
    filter_class = MethodTypeFilter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return MethodTypeListSerializer
        else:
            return MethodTypeCreateUpdateSerializer

    
class AnalysisTypeViewSet(XadminViewSet):
    serializer_class = AnalysisTypeListSerializer
    queryset = AnalysisType.objects.all().order_by('-pk')
    filter_class = AnalysisTypeFilter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return AnalysisTypeListSerializer
        else:
            return AnalysisTypeCreateUpdateSerializer

    
class MatrixViewSet(XadminViewSet):
    serializer_class = MatrixListSerializer
    queryset = Matrix.objects.all().order_by('-pk')
    filter_class = MatrixFilter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return MatrixListSerializer
        else:
            return MatrixCreateUpdateSerializer

    
class SourceViewSet(XadminViewSet):
    serializer_class = SourceListSerializer
    queryset = Source.objects.all().order_by('-pk')
    filter_class = SourceFilter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return SourceListSerializer
        else:
            return SourceCreateUpdateSerializer

    
class EluentViewSet(XadminViewSet):
    serializer_class = EluentListSerializer
    queryset = Eluent.objects.all().order_by('-pk')
    filter_class = EluentFilter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return EluentListSerializer
        else:
            return EluentCreateUpdateSerializer

    
class UnitViewSet(XadminViewSet):
    serializer_class = UnitListSerializer
    queryset = Unit.objects.all().order_by('-pk')
    filter_class = UnitFilter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return UnitListSerializer
        else:
            return UnitCreateUpdateSerializer

    
class ConcUnitViewSet(XadminViewSet):
    serializer_class = ConcUnitListSerializer
    queryset = ConcUnit.objects.all().order_by('-pk')
    filter_class = ConcUnitFilter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return ConcUnitListSerializer
        else:
            return ConcUnitCreateUpdateSerializer

    
class DeviceViewSet(XadminViewSet):
    serializer_class = DeviceListSerializer
    queryset = Device.objects.all().order_by('-pk')
    filter_class = DeviceFilter
    search_fields = ["name","model","sn"]

    def get_serializer_class(self):
        if self.action == "list":
            return DeviceListSerializer
        else:
            return DeviceCreateUpdateSerializer

    
class CompoundCodeCounterViewSet(XadminViewSet):
    serializer_class = CompoundCodeCounterListSerializer
    queryset = CompoundCodeCounter.objects.all().order_by('-pk')
    filter_class = CompoundCodeCounterFilter
    search_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return CompoundCodeCounterListSerializer
        else:
            return CompoundCodeCounterCreateUpdateSerializer

    
class CompoundTagViewSet(XadminViewSet):
    serializer_class = CompoundTagListSerializer
    queryset = CompoundTag.objects.all().order_by('-pk')
    filter_class = CompoundTagFilter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return CompoundTagListSerializer
        else:
            return CompoundTagCreateUpdateSerializer

    
class CompoundViewSet(XadminViewSet):
    serializer_class = CompoundListSerializer
    queryset = Compound.objects.all().order_by('-pk')
    filter_class = CompoundFilter
    search_fields = ["code","name_cn","name_en","cas","formula","chemical_prop","physical_prop"]

    def get_serializer_class(self):
        if self.action == "list":
            return CompoundListSerializer
        else:
            return CompoundCreateUpdateSerializer

    
class ExperimentViewSet(XadminViewSet):
    serializer_class = ExperimentListSerializer
    queryset = Experiment.objects.all().order_by('-pk')
    filter_class = ExperimentFilter
    search_fields = ["location"]

    def get_serializer_class(self):
        if self.action == "list":
            return ExperimentListSerializer
        else:
            return ExperimentCreateUpdateSerializer

    
class SpectrumTagViewSet(XadminViewSet):
    serializer_class = SpectrumTagListSerializer
    queryset = SpectrumTag.objects.all().order_by('-pk')
    filter_class = SpectrumTagFilter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return SpectrumTagListSerializer
        else:
            return SpectrumTagCreateUpdateSerializer

    
class SpectrumViewSet(XadminViewSet):
    serializer_class = SpectrumListSerializer
    queryset = Spectrum.objects.all().order_by('-pk')
    filter_class = SpectrumFilter
    search_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return SpectrumListSerializer
        else:
            return SpectrumCreateUpdateSerializer

    
class QuantMethodCodeCounterViewSet(XadminViewSet):
    serializer_class = QuantMethodCodeCounterListSerializer
    queryset = QuantMethodCodeCounter.objects.all().order_by('-pk')
    filter_class = QuantMethodCodeCounterFilter
    search_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return QuantMethodCodeCounterListSerializer
        else:
            return QuantMethodCodeCounterCreateUpdateSerializer

    
class QuantMethodViewSet(XadminViewSet):
    serializer_class = QuantMethodListSerializer
    queryset = QuantMethod.objects.all().order_by('-pk')
    filter_class = QuantMethodFilter
    search_fields = ["code"]

    def get_serializer_class(self):
        if self.action == "list":
            return QuantMethodListSerializer
        else:
            return QuantMethodCreateUpdateSerializer

    
class CartridgeViewSet(XadminViewSet):
    serializer_class = CartridgeListSerializer
    queryset = Cartridge.objects.all().order_by('-pk')
    filter_class = CartridgeFilter
    search_fields = ["code"]

    def get_serializer_class(self):
        if self.action == "list":
            return CartridgeListSerializer
        else:
            return CartridgeCreateUpdateSerializer
