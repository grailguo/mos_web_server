from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ErectoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "mos_web_server.erecto"
    verbose_name = _("Erecto")
