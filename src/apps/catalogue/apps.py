from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig


class CatalogueConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.catalogue"
    verbose_name = _("Catalogue")
