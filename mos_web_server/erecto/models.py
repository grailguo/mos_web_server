from django.db import models
from django.utils.translation import gettext_lazy as _

from mos_web_server.users.models import BaseModel


# Create your models here.
class MethodType(BaseModel):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return str(self.name).upper()

    class Meta:
        verbose_name = _('method type')
        verbose_name_plural = _('method types')

    pass


class AnalysisType(BaseModel):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('analysis type')
        verbose_name_plural = _('analysis types')

    pass


class Matrix(BaseModel):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return str(self.name).upper()

    class Meta:
        verbose_name = _('matrix')
        verbose_name_plural = _('matrixs')

    pass


class Source(BaseModel):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return str(self.name).upper()

    class Meta:
        verbose_name = _('source')
        verbose_name_plural = _('sources')

    pass


class Eluent(BaseModel):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return str(self.name).upper()

    class Meta:
        verbose_name = _('eluent')
        verbose_name_plural = _('eluents')

    pass


class Unit(BaseModel):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('unit')
        verbose_name_plural = _('units')

    pass


class ConcUnit(BaseModel):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('conc unit')
        verbose_name_plural = _('conc units')

    pass
