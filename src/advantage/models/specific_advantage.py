from django.utils.translation import gettext_lazy as _
from advantage.models.abstracts import Advantage, Purposes


class FirmAdvantage(Advantage):
    """Inheritor of Advantage representing advantage of Firm specifically"""
    purpose = Purposes.FIRM

    class Meta:
        verbose_name = _("Firm advantage")
        verbose_name_plural = _("Firm advantages")
        db_table = "firm_advantages"

    def __str__(self):
        return "".join([str(self.id), ": ", self.title])


class MaterialAdvantage(Advantage):
    """Inheritor of Advantage representing advantage of Material specifically"""
    purpose = Purposes.MATERIAL

    class Meta:
        verbose_name = _("Material advantage")
        verbose_name_plural = _("Material advantages")
        db_table = "material_advantages"

    def __str__(self):
        return "".join([str(self.id), ": ", self.title])
