from admin_ordering.models import OrderableModel
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from sortedm2m.fields import SortedManyToManyField

from erecto.models import AnalysisType, Source, MethodType
from reparo.models import Device


# Create your models here.
class BaseModel(models.Model):
    objects = models.Manager
    description = models.TextField(blank=True, null=True, default='')
    activated = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s (#%s)" % (self.__class__.__name__, self.pk)

    @property
    def desc(self):
        if len(self.description) > 20:
            return self.description[:17] + '...'
        else:
            return self.description

    class Meta:
        abstract = True

    pass


class Polarity(models.TextChoices):
    POLARITY_NEG = 'NEG', _('NEG')
    POLARITY_POS = 'POS', _('POS')
    POLARITY_ALL = 'ALL', _('ALL')
    pass


class QuantType(models.TextChoices):
    QUANT_TYPE_IS = 'IS', _('IS')
    QUANT_TYPE_ES = 'ES', _('ES')
    pass


class CompoundCodeCounter(models.Model):
    objects = models.Manager

    pass


def next_compound_code():
    if len(CompoundCodeCounter.objects.all()):
        return str(CompoundCodeCounter.objects.last().id + 100001)
    else:
        return str(100001)
    pass


class CompoundTag(BaseModel):
    # organization = models.ForeignKey(Organization, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('compound tag')
        verbose_name_plural = _('compound tags')

    pass


class Compound(BaseModel):
    # organization = models.ForeignKey(Organization, null=True, blank=True, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, unique=True)
    name_cn = models.CharField(max_length=100, blank=True, default='')
    name_en = models.CharField(max_length=100, blank=True, default='')
    cas = models.CharField(max_length=100, blank=True, default='')
    mass = models.DecimalField(max_digits=12, decimal_places=6)
    formula = models.CharField(max_length=100, blank=True, default='')
    chemical_prop = models.CharField(max_length=100, blank=True, default='')
    physical_prop = models.CharField(max_length=100, blank=True, default='')
    structural_formula = models.ImageField(upload_to='uploads/structural_formula/%Y/%m/%d/%H/%M/%S/',
                                           max_length=1024, blank=True, default='')
    safety_data_sheet = models.FileField(upload_to='uploads/safety_data_sheet/%Y/%Y/%m/%d/%H/%M/%S/',
                                         max_length=1024, blank=True, default='')
    extra_data = models.JSONField(blank=True, null=False, default=dict)
    compound_tag = models.ManyToManyField(CompoundTag, )

    def __str__(self):
        return '{}-({})'.format(self.code, self.name_cn)

    def compound_tags(self):
        return ', '.join([a.name for a in self.compound_tag.all()])

    compound_tags.short_description = _('compound tags')

    class Meta:
        verbose_name = _('compound')
        verbose_name_plural = _('compounds')

    pass


class Experiment(BaseModel):
    # organization = models.ForeignKey(Organization, null=True, blank=True, on_delete=models.SET_NULL)
    compound = models.ForeignKey(Compound, on_delete=models.CASCADE)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    # dissociation_method = models.CharField(max_length=100, blank=True, default='CID')
    location = models.CharField(max_length=100, blank=True, default='')
    temperature = models.DecimalField(max_digits=12, decimal_places=6)
    humidity = models.DecimalField(max_digits=12, decimal_places=6)

    class Meta:
        verbose_name = _('experiment')
        verbose_name_plural = _('experiments')

    pass


class SpectrumTag(BaseModel):
    # organization = models.ForeignKey(Organization, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('spectrum tag')
        verbose_name_plural = _('spectrum tags')

    pass


class Spectrum(OrderableModel, BaseModel):
    # organization = models.ForeignKey(Organization, null=True, blank=True, on_delete=models.SET_NULL)
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    compound = models.ForeignKey(Compound, on_delete=models.CASCADE)
    precursor_mz = models.DecimalField(max_digits=12, decimal_places=6)
    method_type = models.ForeignKey(MethodType, on_delete=models.CASCADE)
    polarity = models.TextField(choices=Polarity.choices)
    cid_q = models.DecimalField(max_digits=12, decimal_places=6)
    cid_amp = models.DecimalField(max_digits=12, decimal_places=6)
    inj_lmco_mz = models.PositiveSmallIntegerField(
        default=50, validators=[MinValueValidator(0), MaxValueValidator(1000)])
    iso1_amp = models.DecimalField(max_digits=12, decimal_places=6)
    iso2_amp = models.DecimalField(max_digits=12, decimal_places=6)
    average = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    peaks = models.JSONField(blank=True, null=False, default=dict)
    extra_params = models.JSONField(blank=True, null=False, default=dict)
    precursor_mz_ms3 = models.DecimalField(max_digits=12, decimal_places=6, default=0)
    iso_amp_ms3 = models.DecimalField(max_digits=12, decimal_places=6, default=0)
    cid_amp_ms3 = models.DecimalField(max_digits=12, decimal_places=6, default=0)
    scan_mass_start = models.PositiveSmallIntegerField(
        default=50, validators=[MinValueValidator(0), MaxValueValidator(1000)])
    scan_mass_end = models.PositiveSmallIntegerField(
        default=1000, validators=[MinValueValidator(0), MaxValueValidator(5000)])
    spectrum_tag = models.ManyToManyField(SpectrumTag, )

    def save(self, *args, **kwargs):
        self.compound = self.experiment.compound
        super().save(*args, **kwargs)

    def spectrum_tags(self):
        return ', '.join([a.name for a in self.spectrum_tag.all()])

    spectrum_tags.short_description = _('spectrum tags')

    class Meta(OrderableModel.Meta):
        verbose_name = _('spectrum')
        verbose_name_plural = _('spectra')

    pass


class QuantMethodCodeCounter(models.Model):
    objects = models.Manager

    pass


def next_quant_method_code():
    if len(QuantMethodCodeCounter.objects.all()):
        return 'Q{}'.format(QuantMethodCodeCounter.objects.last().id + 10001)
    else:
        return 'Q10001'
    pass


class QuantMethod(BaseModel):
    # organization = models.ForeignKey(Organization, null=True, blank=True, on_delete=models.SET_NULL)
    code = models.CharField(max_length=6, unique=True)
    quant_type = models.TextField(choices=QuantType.choices, blank=False, null=False, )
    target_spectrum = models.ForeignKey(Spectrum, related_name='target_spectrum', on_delete=models.CASCADE)
    in_std_spectrum = models.ForeignKey(Spectrum, related_name='in_std_spectrum', blank=True, null=True,
                                        on_delete=models.CASCADE)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = _('quant method')
        verbose_name_plural = _('quant methods')

    pass


class Cartridge(BaseModel):
    # organization = models.ForeignKey(Organization, null=True, blank=True, on_delete=models.CASCADE)
    code = models.CharField(max_length=128, unique=True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    analysis_type = models.ForeignKey(AnalysisType, on_delete=models.CASCADE)
    polarity = models.TextField(choices=Polarity.choices, blank=False, null=False, )
    pre_spary_time = models.PositiveIntegerField(default=500, )
    spray_voltage_pos = models.PositiveIntegerField(default=4500, )
    spray_voltage_neg = models.PositiveIntegerField(default=3000, )
    compound = SortedManyToManyField(Compound, blank=True)
    compound_tag = models.ManyToManyField(CompoundTag, blank=True)
    quant_method = SortedManyToManyField(QuantMethod, blank=True)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = _('cartridge')
        verbose_name_plural = _('cartridges')

    pass
