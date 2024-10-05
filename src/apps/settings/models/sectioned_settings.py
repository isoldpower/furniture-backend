from django.utils.translation import gettext_lazy as _
from django.db import models

from .abstracts import Settings, SettingsSections


class SectionedSettings(Settings):
    """Inheritor of Settings, related to the specific section"""
    section = models.CharField(choices=SettingsSections.choices, default=SettingsSections.GLOBAL, editable=False,
                               verbose_name=_("Related section"))

    class Meta:
        ordering = ["verbose_name"]

    def __str__(self):
        return self.verbose_name


class GlobalSettings(SectionedSettings):
    """Inheritor of SectionedSettings, related to the Global section"""
    section = SettingsSections.GLOBAL

    class Meta:
        verbose_name = _("Global Settings")
        verbose_name_plural = _("Global Settings")


class HeroSettings(SectionedSettings):
    """Inheritor of SectionedSettings, related to the Hero section"""
    section = SettingsSections.HERO

    class Meta:
        verbose_name = _("Hero Settings")
        verbose_name_plural = _("Hero Settings")


class AboutSettings(SectionedSettings):
    """Inheritor of SectionedSettings, related to the About section"""
    section = SettingsSections.ABOUT

    class Meta:
        verbose_name = _("About Settings")
        verbose_name_plural = _("About Settings")


class LinksSettings(SectionedSettings):
    """Inheritor of SectionedSettings, related to the Links section"""
    section = SettingsSections.LINKS

    class Meta:
        verbose_name = _("Links Settings")
        verbose_name_plural = _("Links Settings")


class AddressSettings(SectionedSettings):
    """Inheritor of SectionedSettings, related to the Address section"""
    section = SettingsSections.ADDRESS

    class Meta:
        verbose_name = _("Address Settings")
        verbose_name_plural = _("Address Settings")


class CatalogSettings(SectionedSettings):
    """Inheritor of SectionedSettings, related to the Catalog section"""
    section = SettingsSections.CATALOG

    class Meta:
        verbose_name = _("Catalog Settings")
        verbose_name_plural = _("Catalog Settings")


class QuoteSettings(SectionedSettings):
    """Inheritor of SectionedSettings, related to the Quote section"""
    section = SettingsSections.QUOTE

    class Meta:
        verbose_name = _("Quote Settings")
        verbose_name_plural = _("Quote Settings")
