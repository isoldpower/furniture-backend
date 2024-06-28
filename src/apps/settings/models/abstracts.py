from django.utils.translation import gettext_lazy as _
from django.db import models

import uuid


class SettingsSections(models.TextChoices):
    """TextChoices of settings sections supported"""
    GLOBAL = "global",
    HERO = "home_hero",
    QUOTE = "home_quote",
    ABOUT = "about_page",
    ADDRESS = "footer_address",
    CATALOG = "catalog_page",
    LINKS = "socials_links"


class Settings(models.Model):
    """Model representing website static content setting"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("Settings id"))
    verbose_name = models.CharField(default='Название', verbose_name=_("Name"))
    key = models.CharField(max_length=255, unique=True, default='FIELD_KEY', verbose_name=_("Unique key"))
    value = models.TextField(default='', verbose_name=_("Settings value"))

    class Meta:
        abstract = True
        db_table = 'settings'
