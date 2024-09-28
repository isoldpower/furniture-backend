from django.utils.translation import gettext_lazy as _
from django.db import models

from .abstracts import AbstractImage
from ..services.image import get_compressed_image, get_compressed_name


class DoublesidedImage(AbstractImage):
    """Inheritor of Image model representing image with several resolutions"""
    low_src = models.ImageField(upload_to="thumbnails/", editable=False, verbose_name=_("Low resolution"))

    def save(self, *args, **kwargs):
        """Overriding save method to save low resolution image"""
        img_thumb = get_compressed_image(self.src)
        name = get_compressed_name(self.src)
        self.low_src.save(name, img_thumb, save=False)
        super(DoublesidedImage, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = "doublesided_images"
        verbose_name = _("Doublesided image")
        verbose_name_plural = _("Doublesided images")

    def __str__(self):
        return str(self.verbose_name)
