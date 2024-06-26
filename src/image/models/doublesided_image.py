from django.utils.translation import gettext_lazy as _
from django.db import models

from image.models.abstracts import Image


class DoublesidedImage(Image):
    """Inheritor of Image model representing image with several resolutions"""
    low_src = models.ImageField(upload_to="images/", verbose_name=_("Low resolution"))

    class Meta:
        ordering = ["id"]
        db_table = "doublesided_images"
        verbose_name = _("Doublesided image")
        verbose_name_plural = _("Doublesided images")

    def __str__(self):
        return str(self.verbose_name)
