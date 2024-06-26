from django.utils.translation import gettext_lazy as _
from django.db import models


class Material(models.Model):
    """Model representing material used to create furniture"""
    id = models.AutoField(primary_key=True, editable=False, unique=True, verbose_name=_("Material id"))
    title = models.CharField(max_length=60, verbose_name=_("Title"))
    first_paragraph = models.TextField(blank=False, null=False, verbose_name=_("Main paragraph"))
    second_paragraph = models.TextField(blank=False, null=False, verbose_name=_("Secondary paragraph"))
    href_postfix = models.CharField(max_length=30, unique=True, null=False, blank=False,
                                    verbose_name=_("Href postfix"), default="/postfix")

    class Meta:
        db_table = "materials"
        abstract = True
