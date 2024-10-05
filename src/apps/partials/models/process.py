from django.utils.translation import gettext_lazy as _
from django.db import models


class Process (models.Model):
    id = models.AutoField(primary_key=True, unique=True, editable=False, verbose_name=_("Process id"))
    order = models.IntegerField(unique=True, verbose_name=_("Process order"))
    paragraph = models.TextField(max_length=255, verbose_name=_("Process paragraph"))
    image = models.ForeignKey('DoublesidedImage', on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Process image"))

    class Meta:
        verbose_name = _("Process")
        verbose_name_plural = _("Processes")
        ordering = ['order']

    def __str__(self):
        return self.paragraph[:30]
