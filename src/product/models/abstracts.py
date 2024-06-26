from django.utils.translation import gettext_lazy as _
from django.db import models


class Product(models.Model):
    """Model representing general data of a product"""
    id = models.AutoField(primary_key=True, editable=False, unique=True, verbose_name=_("Product id"))
    title = models.CharField(max_length=60, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"))
    preparation_time = models.CharField(max_length=60, verbose_name=_("Time to produce"))
    estimated_cost = models.CharField(max_length=60, verbose_name=_("Estimated cost"))
    href_postfix = models.CharField(max_length=30, unique=True, null=False, blank=False, verbose_name=_("Href postfix"))

    class Meta:
        db_table = 'products'
        abstract = True
