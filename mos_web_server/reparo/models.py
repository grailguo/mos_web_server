from django.db import models
from django.utils.translation import gettext_lazy as _

from mos_web_server.users.models import BaseModel, Organization


# Create your models here.
class Device(BaseModel):
    organization = models.ForeignKey(Organization, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    sn = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return str(self.sn).upper()

    class Meta:
        verbose_name = _('device')
        verbose_name_plural = _('devices')

    pass
