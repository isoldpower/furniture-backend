from django.utils.translation import gettext_lazy as _
from django.db import models

from catalogue.models.abstracts import AbstractSection
from catalogue.models.stock_product import StockProduct
from image.models.doublesided_image import DoublesidedImage


class StockSection(AbstractSection):
    """Inheritor of AbstractSection model representing a section of StockProducts"""
    preview_image = models.ForeignKey(DoublesidedImage, null=True, on_delete=models.SET_NULL,
                                      verbose_name=_("Preview image"))
    products = models.ManyToManyField(StockProduct, verbose_name=_("Section products"))

    class Meta:
        db_table = 'stock_sections'
        verbose_name = _("Stock section")
        verbose_name_plural = _("Stock sections")

    def __str__(self):
        return str(self.id) + ': ' + str(self.title)
