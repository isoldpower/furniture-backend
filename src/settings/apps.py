from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig


class SettingsConfig(AppConfig):
    name = 'settings'
    verbose_name = _("Settings")
