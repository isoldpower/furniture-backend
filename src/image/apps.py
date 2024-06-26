from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig


class ImageConfig(AppConfig):
    name = 'image'
    verbose_name = _("Image")
    verbose_name_plural = _("Images")
