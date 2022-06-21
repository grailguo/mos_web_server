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


class Device(BaseModel):
    # organization = models.ForeignKey(Organization, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    sn = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return str(self.sn).upper()

    class Meta:
        verbose_name = _('device')
        verbose_name_plural = _('devices')

    pass
