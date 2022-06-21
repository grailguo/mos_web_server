from django_filters import rest_framework as filters
from tyadmin_api.custom import DateFromToRangeFilter
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from erecto.models import MethodType, AnalysisType, Matrix, Source, Eluent, Unit, ConcUnit
from reparo.models import Device
from accio.models import CompoundCodeCounter, CompoundTag, Compound, Experiment, SpectrumTag, Spectrum, QuantMethodCodeCounter, QuantMethod, Cartridge

class PermissionFilter(filters.FilterSet):
    content_type_text = filters.CharFilter(field_name="content_type")

    class Meta:
        model = Permission
        exclude = []

class GroupFilter(filters.FilterSet):

    class Meta:
        model = Group
        exclude = []

class ContentTypeFilter(filters.FilterSet):

    class Meta:
        model = ContentType
        exclude = []

class MethodTypeFilter(filters.FilterSet):
    updated = DateFromToRangeFilter(field_name="updated")
    created = DateFromToRangeFilter(field_name="created")

    class Meta:
        model = MethodType
        exclude = []

class AnalysisTypeFilter(filters.FilterSet):
    updated = DateFromToRangeFilter(field_name="updated")
    created = DateFromToRangeFilter(field_name="created")

    class Meta:
        model = AnalysisType
        exclude = []

class MatrixFilter(filters.FilterSet):
    updated = DateFromToRangeFilter(field_name="updated")
    created = DateFromToRangeFilter(field_name="created")

    class Meta:
        model = Matrix
        exclude = []

class SourceFilter(filters.FilterSet):
    updated = DateFromToRangeFilter(field_name="updated")
    created = DateFromToRangeFilter(field_name="created")

    class Meta:
        model = Source
        exclude = []

class EluentFilter(filters.FilterSet):
    updated = DateFromToRangeFilter(field_name="updated")
    created = DateFromToRangeFilter(field_name="created")

    class Meta:
        model = Eluent
        exclude = []

class UnitFilter(filters.FilterSet):
    updated = DateFromToRangeFilter(field_name="updated")
    created = DateFromToRangeFilter(field_name="created")

    class Meta:
        model = Unit
        exclude = []

class ConcUnitFilter(filters.FilterSet):
    updated = DateFromToRangeFilter(field_name="updated")
    created = DateFromToRangeFilter(field_name="created")

    class Meta:
        model = ConcUnit
        exclude = []

class DeviceFilter(filters.FilterSet):
    updated = DateFromToRangeFilter(field_name="updated")
    created = DateFromToRangeFilter(field_name="created")

    class Meta:
        model = Device
        exclude = []

class CompoundCodeCounterFilter(filters.FilterSet):

    class Meta:
        model = CompoundCodeCounter
        exclude = []

class CompoundTagFilter(filters.FilterSet):
    updated = DateFromToRangeFilter(field_name="updated")
    created = DateFromToRangeFilter(field_name="created")

    class Meta:
        model = CompoundTag
        exclude = []

class CompoundFilter(filters.FilterSet):
    updated = DateFromToRangeFilter(field_name="updated")
    created = DateFromToRangeFilter(field_name="created")

    class Meta:
        model = Compound
        exclude = ["extra_data","structural_formula","structural_formula","safety_data_sheet"]

class ExperimentFilter(filters.FilterSet):
    compound_text = filters.CharFilter(field_name="compound")
    source_text = filters.CharFilter(field_name="source")
    device_text = filters.CharFilter(field_name="device")
    updated = DateFromToRangeFilter(field_name="updated")
    created = DateFromToRangeFilter(field_name="created")

    class Meta:
        model = Experiment
        exclude = []

class SpectrumTagFilter(filters.FilterSet):
    updated = DateFromToRangeFilter(field_name="updated")
    created = DateFromToRangeFilter(field_name="created")

    class Meta:
        model = SpectrumTag
        exclude = []

class SpectrumFilter(filters.FilterSet):
    experiment_text = filters.CharFilter(field_name="experiment")
    compound_text = filters.CharFilter(field_name="compound")
    method_type_text = filters.CharFilter(field_name="method_type")
    updated = DateFromToRangeFilter(field_name="updated")
    created = DateFromToRangeFilter(field_name="created")

    class Meta:
        model = Spectrum
        exclude = ["peaks", "extra_params",]

class QuantMethodCodeCounterFilter(filters.FilterSet):

    class Meta:
        model = QuantMethodCodeCounter
        exclude = []

class QuantMethodFilter(filters.FilterSet):
    target_spectrum_text = filters.CharFilter(field_name="target_spectrum")
    in_std_spectrum_text = filters.CharFilter(field_name="in_std_spectrum")
    updated = DateFromToRangeFilter(field_name="updated")
    created = DateFromToRangeFilter(field_name="created")

    class Meta:
        model = QuantMethod
        exclude = []

class CartridgeFilter(filters.FilterSet):
    source_text = filters.CharFilter(field_name="source")
    analysis_type_text = filters.CharFilter(field_name="analysis_type")
    updated = DateFromToRangeFilter(field_name="updated")
    created = DateFromToRangeFilter(field_name="created")

    class Meta:
        model = Cartridge
        exclude = []
