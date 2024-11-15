from django.utils.translation import gettext_lazy as _
from django.db import models

from .abstracts import AbstractSection
from .stock_product import StockProduct
from apps.partials.models import DoublesidedImage


class StockSection(AbstractSection):
    """Inheritor of AbstractSection model representing a section of StockProducts"""
    preview_image = models.ForeignKey(DoublesidedImage, null=True, blank=True, on_delete=models.SET_NULL, verbose_name=_("Preview image"))
    products = models.ManyToManyField(StockProduct, null=True, blank=True, verbose_name=_("Section products"))
    visible_in_header = models.BooleanField(default=False, verbose_name=_("Visible in header"))
    visible_in_preview = models.BooleanField(default=False, verbose_name=_("Visible in preview"))

    class Meta:
        db_table = 'stock_sections'
        verbose_name = _("Stock section")
        verbose_name_plural = _("Stock sections")

    def __str__(self):
        return str(self.id) + ': ' + str(self.title)
