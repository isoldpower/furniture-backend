from django.utils.translation import gettext_lazy as _
from django.db import models

from .abstracts import AbstractProduct
from .product_material import ProductMaterial
from apps.partials.models import DoublesidedImage


class StockProduct(AbstractProduct):
    """Inheritor of AbstractProduct model representing a product that is available in catalogue"""
    materials = models.ManyToManyField(ProductMaterial, verbose_name=_("Product materials"))
    images = models.ManyToManyField(DoublesidedImage, null=True, blank=True, verbose_name=_("Product images"))
    important = models.BooleanField(default=False, verbose_name=_("Is important"))

    class Meta:
        db_table = "stock_products"
        verbose_name = _("Stock product")
        verbose_name_plural = _("Stock products")

    def __str__(self):
        importance_sign = '' if self.important else ''
        return str(self.title) + importance_sign
