from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig


class ProductConfig(AppConfig):
    name = 'product'
    verbose_name = _("Product")
