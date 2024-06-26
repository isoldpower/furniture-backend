from django.utils.translation import gettext_lazy as _
from django.db import models

from advantage.models.specific_advantage import MaterialAdvantage
from image.models.doublesided_image import DoublesidedImage
from catalogue.models.abstracts import AbstractMaterial


class ProductMaterial(AbstractMaterial):
    """Inheritor of Material representing detailed material data"""
    advantages = models.ManyToManyField(MaterialAdvantage, verbose_name=_("Material advantages"))
    image = models.ForeignKey(DoublesidedImage, null=True, on_delete=models.SET_NULL, verbose_name=_("Preview image"))
    important = models.BooleanField(default=False, verbose_name=_("Is important"))

    class Meta:
        db_table = "product_materials"
        verbose_name = _("Product material")
        verbose_name_plural = _("Product materials")

    def __str__(self):
        return self.title
