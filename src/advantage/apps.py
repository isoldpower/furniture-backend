from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig


class AdvantageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'advantage'
    verbose_name_plural = _("Advantages")
    verbose_name = _("Advantage")
