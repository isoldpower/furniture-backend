from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig


class PortfolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "apps.portfolio"
    verbose_name = _("Portfolio")
