from django.utils.translation import gettext_lazy as _
from django.db import models

from product.models.detailed_product import DetailedProduct
from section.models.abstracts import Section


class DetailedSection(Section):
    """Inheritor of Section model representing a detailed section data"""
    products = models.ManyToManyField(DetailedProduct, verbose_name=_("Section products"))

    class Meta:
        db_table = 'detailed_sections'
        verbose_name = _("Detailed section")
        verbose_name_plural = _("Detailed sections")

    def __str__(self):
        return str(self.id) + ': ' + str(self.title)
