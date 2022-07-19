from rest_framework import serializers

# Serializers define the API representation.
from mos_web_server.accio.api.serializers import CompoundSerializer
from mos_web_server.flagrate.models import DataTag, Substance, Case, Data


class DataTagSerializer(serializers.HyperlinkedModelSerializer):
    activated = serializers.BooleanField(default=True, initial=True)

    class Meta:
        model = DataTag
        fields = '__all__'

    pass


class SubstanceSerializer(serializers.HyperlinkedModelSerializer):
    compound_code = serializers.ReadOnlyField(source='compound.code', )
    compound_name_cn = serializers.ReadOnlyField(source='compound.name_cn', )
    compound_name_en = serializers.ReadOnlyField(source='compound.name_en', )
    organization_name = serializers.ReadOnlyField(source='organization.name', allow_null=True, )
    conc_unit_name = serializers.ReadOnlyField(source='conc_unit.name', allow_null=True, )

    class Meta:
        model = Substance
        fields = '__all__'

    pass


class CaseSerializer(serializers.HyperlinkedModelSerializer):
    case_code = serializers.ReadOnlyField()
    activated = serializers.BooleanField(default=True, initial=True)
    cartridge_code = serializers.ReadOnlyField(source='cartridge.code', )
    source_name = serializers.ReadOnlyField(source='cartridge.source.name', )
    analysis_type_name = serializers.ReadOnlyField(source='cartridge.analysis_type.name', )
    matrix_name = serializers.ReadOnlyField(source='matrix.name', )
    eluent_name = serializers.ReadOnlyField(source='eluent.name', )
    sample_unit_name = serializers.ReadOnlyField(source='sample_unit.name', )
    organization_name = serializers.ReadOnlyField(source='organization.name', allow_null=True, )
    algorithm_data = serializers.JSONField(default=dict, initial=dict)
    algorithm_parameters = serializers.JSONField(default=dict, initial=dict)
    analysis_parameters = serializers.JSONField(default=dict, initial=dict)
    quant_methods = serializers.JSONField(default=dict, initial=dict)
    config_parameters = serializers.JSONField(default=dict, initial=dict)
    expected_result = serializers.JSONField(default=list, initial=list)

    class Meta:
        model = Case
        fields = '__all__'

    pass


class CaseWithSubstanceSerializer(serializers.HyperlinkedModelSerializer):
    case_code = serializers.ReadOnlyField()
    activated = serializers.BooleanField(default=True, initial=True)
    cartridge_code = serializers.ReadOnlyField(source='cartridge.code', )
    source_name = serializers.ReadOnlyField(source='cartridge.source.name', )
    analysis_type_name = serializers.ReadOnlyField(source='cartridge.analysis_type.name', )
    matrix_name = serializers.ReadOnlyField(source='matrix.name', )
    eluent_name = serializers.ReadOnlyField(source='eluent.name', )
    sample_unit_name = serializers.ReadOnlyField(source='sample_unit.name', )
    organization_name = serializers.ReadOnlyField(source='organization.name', allow_null=True, )
    algorithm_parameters = serializers.JSONField(default=dict, initial=dict)
    analysis_parameters = serializers.JSONField(default=dict, initial=dict)
    config_parameters = serializers.JSONField(default=dict, initial=dict)
    expected_result = serializers.JSONField(default=dict, initial=dict)
    substances = SubstanceSerializer(many=True, read_only=True, )

    class Meta:
        model = Case
        fields = '__all__'

    pass


class DataSerializer(serializers.HyperlinkedModelSerializer):
    activated = serializers.BooleanField(default=True, initial=True)
    case_id = serializers.ReadOnlyField(source='case.id', )
    device_sn = serializers.ReadOnlyField(source='device.sn', )
    data_info = serializers.JSONField(default=dict, initial=dict)
    expected_result = serializers.JSONField(default=dict, initial=dict)
    analysis_result = serializers.JSONField(default=dict, initial=dict)

    class Meta:
        model = Data
        fields = '__all__'

    pass


class DataWithTagSerializer(serializers.HyperlinkedModelSerializer):
    activated = serializers.BooleanField(default=True, initial=True)
    case_id = serializers.ReadOnlyField(source='case.id', )
    device_sn = serializers.ReadOnlyField(source='device.sn', )
    data_tags = DataTagSerializer(many=True, required=False, allow_null=True)
    data_info = serializers.JSONField(default=dict, initial=dict)
    expected_result = serializers.JSONField(default=dict, initial=dict)
    analysis_result = serializers.JSONField(default=dict, initial=dict)
    neg_compounds = CompoundSerializer(many=True, required=False, allow_null=True)
    pos_compounds = CompoundSerializer(many=True, required=False, allow_null=True)

    class Meta:
        model = Data
        fields = '__all__'

    pass
