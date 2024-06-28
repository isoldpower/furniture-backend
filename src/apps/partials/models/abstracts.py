from django.utils.translation import gettext_lazy as _
from django.db import models


class Purposes(models.TextChoices):
    FIRM = "firm",
    MATERIAL = "material"


class AbstractAdvantage(models.Model):
    """Model representing advantage of using something"""
    id = models.AutoField(primary_key=True, editable=False, unique=True, verbose_name=_("Advantage id"))
    title = models.CharField(max_length=60, verbose_name=_("Title"))
    paragraph = models.TextField(blank=False, null=False, verbose_name=_("Main paragraph"))
    purpose = models.CharField(choices=Purposes.choices, default=Purposes.FIRM, verbose_name=_("Scope"))

    class Meta:
        db_table = 'advantages'
        abstract = True

    def __str__(self):
        return "".join([str(self.id), ": ", self.title])


class AbstractImage(models.Model):
    """Class representing basic image data with 'alt' alternative text, image 'src' source and verbose name 'title'"""
    id = models.AutoField(primary_key=True, editable=False, unique=True, verbose_name=_("Image id"))
    verbose_name = models.CharField(max_length=63, unique=True, verbose_name=_("Image title"))
    src = models.ImageField(upload_to="assets/", verbose_name=_("High resolution"))
    alt = models.TextField(blank=True, default="", verbose_name=_("Alternative text"))

    class Meta:
        db_table = "images"
        abstract = True
