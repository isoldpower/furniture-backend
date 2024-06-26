from django.utils.translation import gettext_lazy as _
from django.db import models


class Purposes(models.TextChoices):
    FIRM = "firm",
    MATERIAL = "material"


class Advantage(models.Model):
    """Model representing advantage of using something"""
    id = models.AutoField(primary_key=True, editable=False, unique=True, verbose_name=_("Advantage id"))
    title = models.CharField(max_length=60, verbose_name=_("Title"))
    paragraph = models.TextField(blank=False, null=False, verbose_name=_("Main paragraph"))
    purpose = models.CharField(choices=Purposes.choices, default=Purposes.FIRM, verbose_name=_("Scope"))

    class Meta:
        db_table = 'advantages'
        abstract = True
