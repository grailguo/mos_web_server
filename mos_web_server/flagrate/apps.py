from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FlagrateConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "mos_web_server.flagrate"
    verbose_name = _("Flagrate")
