from django.utils.translation import gettext_lazy as _
from django.db import models

from .abstracts import AbstractMaterial
from apps.partials.models import MaterialAdvantage, DoublesidedImage


class ProductMaterial(AbstractMaterial):
    """Inheritor of Material representing detailed material data"""
    advantages = models.ManyToManyField(MaterialAdvantage, null=True, blank=True, verbose_name=_("Material advantages"))
    image = models.ForeignKey(DoublesidedImage, null=True, blank=True, on_delete=models.SET_NULL, verbose_name=_("Preview image"))
    important = models.BooleanField(default=False,  verbose_name=_("Is important"))

    class Meta:
        db_table = "product_materials"
        verbose_name = _("Product material")
        verbose_name_plural = _("Product materials")

    def __str__(self):
        return self.title
