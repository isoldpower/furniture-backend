from django.utils.translation import gettext_lazy as _
from django.db import models

from image.models.doublesided_image import DoublesidedImage


class Section(models.Model):
    """Model representing a products section"""
    id = models.AutoField(primary_key=True, editable=False, unique=True, verbose_name=_("Section id"))
    title = models.CharField(max_length=60, verbose_name=_("Title"))
    paragraph = models.TextField(blank=True, null=True, verbose_name=_("Paragraph"))
    preview_image = models.ForeignKey(DoublesidedImage, null=True, on_delete=models.SET_NULL,
                                      verbose_name=_("Preview image"))
    href_postfix = models.CharField(max_length=30, unique=True, null=False, blank=False, verbose_name=_("Href postfix"))

    class Meta:
        db_table = 'sections'
        abstract = True
