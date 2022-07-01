from rest_framework import serializers

from mos_web_server.erecto.models import MethodType, AnalysisType, Matrix, Source, Eluent, ConcUnit, Unit


# Create your api serializers here.
# Serializers define the API representation.
class MethodTypeSerializer(serializers.HyperlinkedModelSerializer):
    activated = serializers.BooleanField(default=True, initial=True)

    class Meta:
        model = MethodType
        fields = '__all__'

    pass


class AnalysisTypeSerializer(serializers.HyperlinkedModelSerializer):
    activated = serializers.BooleanField(default=True, initial=True)

    class Meta:
        model = AnalysisType
        fields = '__all__'

    pass


class MatrixSerializer(serializers.HyperlinkedModelSerializer):
    activated = serializers.BooleanField(default=True, initial=True)

    class Meta:
        model = Matrix
        fields = '__all__'

    pass


class SourceSerializer(serializers.HyperlinkedModelSerializer):
    activated = serializers.BooleanField(default=True, initial=True)

    class Meta:
        model = Source
        fields = '__all__'

    pass


class EluentSerializer(serializers.HyperlinkedModelSerializer):
    activated = serializers.BooleanField(default=True, initial=True)

    class Meta:
        model = Eluent
        fields = '__all__'

    pass


class UnitSerializer(serializers.HyperlinkedModelSerializer):
    activated = serializers.BooleanField(default=True, initial=True)

    class Meta:
        model = Unit
        fields = '__all__'

    pass


class ConcUnitSerializer(serializers.HyperlinkedModelSerializer):
    activated = serializers.BooleanField(default=True, initial=True)

    class Meta:
        model = ConcUnit
        fields = '__all__'

    pass
