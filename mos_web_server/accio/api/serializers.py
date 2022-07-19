from rest_framework import serializers

from mos_web_server.accio.models import CompoundTag, Compound, Experiment, SpectrumTag, Spectrum, QuantMethod, \
    Cartridge


# Create your api serializers here.
# Serializers define the API representation.
class CompoundTagSerializer(serializers.HyperlinkedModelSerializer):
    activated = serializers.BooleanField(default=True, initial=True)

    class Meta:
        model = CompoundTag
        fields = '__all__'

    pass


class CompoundSerializer(serializers.HyperlinkedModelSerializer):
    activated = serializers.BooleanField(default=True, initial=True)

    class Meta:
        model = Compound
        fields = '__all__'

    pass


class ExperimentSerializer(serializers.HyperlinkedModelSerializer):
    activated = serializers.BooleanField(default=True, initial=True)

    class Meta:
        model = Experiment
        fields = '__all__'

    pass


class SpectrumTagSerializer(serializers.HyperlinkedModelSerializer):
    activated = serializers.BooleanField(default=True, initial=True)

    class Meta:
        model = SpectrumTag
        fields = '__all__'

    pass


class SpectrumSerializer(serializers.HyperlinkedModelSerializer):
    activated = serializers.BooleanField(default=True, initial=True)

    class Meta:
        model = Spectrum
        fields = '__all__'

    pass


class QuantMethodSerializer(serializers.HyperlinkedModelSerializer):
    activated = serializers.BooleanField(default=True, initial=True)

    class Meta:
        model = QuantMethod
        fields = '__all__'

    pass


class CartridgeSerializer(serializers.HyperlinkedModelSerializer):
    activated = serializers.BooleanField(default=True, initial=True)

    class Meta:
        model = Cartridge
        fields = '__all__'

    pass
