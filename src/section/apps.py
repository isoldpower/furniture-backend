from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig


class SectionConfig(AppConfig):
    name = 'section'
    verbose_name = _("Section")
