from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from mos_web_server.accio.models import Cartridge, Compound
from mos_web_server.erecto.models import Matrix, Unit, Eluent, ConcUnit
from mos_web_server.reparo.models import Device
from mos_web_server.users.models import BaseModel, Organization


class DataTag(BaseModel):
    name = models.CharField(max_length=128, unique=True)
    organization = models.ForeignKey(Organization, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('data tag')
        verbose_name_plural = _('data tags')

    pass


class Case(BaseModel):
    organization = models.ForeignKey(Organization, null=True, blank=True, on_delete=models.CASCADE)
    matrix = models.ForeignKey(Matrix, on_delete=models.CASCADE)
    cartridge = models.ForeignKey(Cartridge, on_delete=models.CASCADE)
    sample_amount = models.DecimalField(max_digits=12, decimal_places=6)
    sample_unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    eluent = models.ForeignKey(Eluent, on_delete=models.CASCADE)
    algorithm_parameters = models.JSONField(blank=True, null=False, default=dict)
    analysis_parameters = models.JSONField(blank=True, null=False, default=dict)
    config_parameters = models.JSONField(blank=True, null=False, default=dict)
    expected_result = models.JSONField(blank=True, null=False, default=dict)

    def case_code(self):
        return str('CASE_#{}').format(self.pk)

    case_code.admin_order_field = 'id'  # Allows column order sorting
    case_code.short_description = _('Case Code')  # Renames column head

    def analysis_type(self):
        return self.cartridge.analysis_type

    analysis_type.admin_order_field = 'cartridge'  # Allows column order sorting
    analysis_type.short_description = _('Analysis Type')  # Renames column head

    class Meta:
        verbose_name = _('case')
        verbose_name_plural = _('cases')

    pass


class Substance(BaseModel):
    organization = models.ForeignKey(Organization, null=True, blank=True, on_delete=models.SET_NULL)
    case = models.ForeignKey(Case, related_name='substances', on_delete=models.CASCADE)
    compound = models.ForeignKey(Compound, on_delete=models.CASCADE)
    concentration = models.DecimalField(max_digits=12, decimal_places=6)
    conc_unit = models.ForeignKey(ConcUnit, on_delete=models.CASCADE)

    def __str__(self):
        return self.compound.name_cn

    def compound_name(self):
        return self.compound.name_cn

    class Meta:
        verbose_name = _('substance')
        verbose_name_plural = _('substances')

    pass


class Data(BaseModel):
    organization = models.ForeignKey(Organization, null=True, blank=True, on_delete=models.SET_NULL)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    mrzfile = models.FileField(upload_to='uploads/mrzfiles/%Y/%m/%d/%H/%M/%S/', max_length=1024, blank=True, default='')
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    data_info = models.JSONField(blank=True, null=False, default=dict)
    result = models.JSONField(blank=True, null=False, default=dict)
    status = models.BooleanField(default=True)
    data_tags = models.ManyToManyField(DataTag, )

    def __str__(self):
        return self.mrzfile.name

    def data_tag_list(self):
        return ', '.join([a.name for a in self.data_tags.all()])

    data_tags.short_description = _('data tags')

    class Meta:
        verbose_name = _('data')
        verbose_name_plural = _('data')

    pass
