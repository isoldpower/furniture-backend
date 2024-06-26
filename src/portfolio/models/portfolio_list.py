from django.utils.translation import gettext_lazy as _
from django.db import models

from image.models.doublesided_image import DoublesidedImage


class PortfolioItem(models.Model):
    """Model representing list of images presented in Portfolio section of website"""
    id = models.AutoField(primary_key=True, unique=True, editable=False, verbose_name=_("Item id"))
    image = models.OneToOneField(DoublesidedImage, on_delete=models.CASCADE, verbose_name=_("Image"))

    class Meta:
        db_table = "portfolio_list"
        verbose_name = _("Portfolio item")
        verbose_name_plural = _("Portfolio items")

    def __str__(self):
        return str(self.id) + ": " + self.image.verbose_name
