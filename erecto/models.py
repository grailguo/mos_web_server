from django.db import models
from django.utils.translation import gettext_lazy as _


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
