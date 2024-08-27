from django.utils.translation import gettext_lazy as _
from django.db import models


class Process (models.Model):
    id = models.AutoField(primary_key=True, unique=True, editable=False, verbose_name=_("Process id"))
    order = models.IntegerField(unique=True, verbose_name=_("Process order"))
    title = models.CharField(max_length=255, unique=True, verbose_name=_("Process title"))
    paragraph = models.TextField(verbose_name=_("Process paragraph"))

    class Meta:
        verbose_name = _("Process")
        verbose_name_plural = _("Processes")
        ordering = ['order']

    def __str__(self):
        return self.title
