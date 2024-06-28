from django.utils.translation import gettext_lazy as _
from .abstracts import Purposes, AbstractAdvantage


class FirmAdvantage(AbstractAdvantage):
    """Inheritor of Advantage representing advantage of Firm specifically"""
    purpose = Purposes.FIRM

    class Meta:
        verbose_name = _("Firm advantage")
        verbose_name_plural = _("Firm advantages")
        db_table = "firm_advantages"


class MaterialAdvantage(AbstractAdvantage):
    """Inheritor of Advantage representing advantage of Material specifically"""
    purpose = Purposes.MATERIAL

    class Meta:
        verbose_name = _("Material advantage")
        verbose_name_plural = _("Material advantages")
        db_table = "material_advantages"
