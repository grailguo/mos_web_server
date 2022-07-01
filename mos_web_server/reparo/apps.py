from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ReparoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "mos_web_server.reparo"
    verbose_name = _("Reparo")
