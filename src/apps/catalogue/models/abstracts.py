from django.utils.translation import gettext_lazy as _
from django.db import models


class AbstractMaterial(models.Model):
    """Model representing material used to create furniture"""
    id = models.AutoField(primary_key=True, editable=False, unique=True, verbose_name=_("id"))
    title = models.CharField(max_length=60, verbose_name=_("Title"))
    first_paragraph = models.TextField(blank=False, null=False, verbose_name=_("Main paragraph"))
    second_paragraph = models.TextField(blank=False, null=False, verbose_name=_("Secondary paragraph"))
    href_postfix = models.CharField(max_length=30, unique=True, null=False, blank=False,
                                    verbose_name=_("Href postfix"), default="/postfix")

    class Meta:
        abstract = True


class AbstractProduct(models.Model):
    """Model representing general data of a product"""
    id = models.AutoField(primary_key=True, editable=False, unique=True, verbose_name=_("id"))
    title = models.CharField(max_length=60, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"))
    preparation_time = models.CharField(max_length=60, verbose_name=_("Time to produce"))
    estimated_cost = models.CharField(max_length=60, verbose_name=_("Estimated cost"))
    href_postfix = models.CharField(max_length=30, unique=True, null=False, blank=False, verbose_name=_("Href postfix"))

    class Meta:
        abstract = True


class AbstractSection(models.Model):
    """Model representing products section"""
    id = models.AutoField(primary_key=True, editable=False, unique=True, verbose_name=_("id"))
    title = models.CharField(max_length=60, verbose_name=_("Title"))
    paragraph = models.TextField(blank=True, null=True, verbose_name=_("Paragraph"))
    href_postfix = models.CharField(max_length=30, unique=True, null=False, blank=False, verbose_name=_("Href postfix"))

    class Meta:
        abstract = True
