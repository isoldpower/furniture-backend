from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig


class PartialsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.partials'
    verbose_name = _("Partials")
