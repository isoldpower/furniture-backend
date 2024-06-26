from django.utils.translation import gettext_lazy as _
from django.db import models

from image.models.doublesided_image import DoublesidedImage
from material.models.detailed_material import DetailedMaterial
from product.models.abstracts import Product


class DetailedProduct(Product):
    """Inheritor of Product model representing a detailed product data"""
    materials = models.ManyToManyField(DetailedMaterial, verbose_name=_("Product materials"))
    images = models.ManyToManyField(DoublesidedImage, verbose_name=_("Product images"))
    is_important = models.BooleanField(default=False, verbose_name=_("Is important"))

    class Meta:
        db_table = 'detailed_products'
        verbose_name = _("Detailed product")
        verbose_name_plural = _("Detailed products")

    def __str__(self):
        importance_sign = '' if self.is_important else ''
        return str(self.title) + importance_sign
