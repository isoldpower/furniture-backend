from django.utils.translation import gettext_lazy as _
from django.db import models


class Image(models.Model):
    """Class representing basic image data with 'alt' alternative text, image 'src' source and verbose name 'title'"""
    id = models.AutoField(primary_key=True, editable=False, unique=True, verbose_name=_("Image id"))
    verbose_name = models.CharField(max_length=63, unique=True, verbose_name=_("Image title"))
    src = models.ImageField(upload_to="images/", verbose_name=_("High resolution"))
    alt = models.TextField(blank=True, default="", verbose_name=_("Alternative text"))

    class Meta:
        db_table = "images"
        abstract = True
