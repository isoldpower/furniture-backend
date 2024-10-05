from django.utils.translation import gettext_lazy as _
from django.db import models

from .abstracts import Purposes, AbstractAdvantage


class FirmAdvantageManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(purpose=Purposes.FIRM)


class FirmAdvantage(AbstractAdvantage):
    """Inheritor of Advantage representing advantage of Firm specifically"""
    purpose = Purposes.FIRM

    objects = FirmAdvantageManager()

    class Meta:
        proxy = True
        verbose_name = _("Firm advantage")
        verbose_name_plural = _("Firm advantages")
        db_table = "firm_advantages"


class MaterialAdvantageManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(purpose=Purposes.MATERIAL)


class MaterialAdvantage(AbstractAdvantage):
    """Inheritor of Advantage representing advantage of Material specifically"""
    purpose = Purposes.MATERIAL

    objects = MaterialAdvantageManager()

    class Meta:
        proxy = True
        verbose_name = _("Material advantage")
        verbose_name_plural = _("Material advantages")
        db_table = "material_advantages"
