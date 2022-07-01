from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AccioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "mos_web_server.accio"
    verbose_name = _("Accio")
