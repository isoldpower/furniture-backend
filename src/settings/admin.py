from django.contrib import admin

from settings.models.sectioned_settings import QuoteSettings, GlobalSettings, HeroSettings, \
    AboutSettings, LinksSettings, AddressSettings, CatalogSettings


class SectionedSettingsAdmin(admin.ModelAdmin):
    list_display = ["verbose_name", "key", "value"]


@admin.register(GlobalSettings)
class GlobalSettingsAdmin(SectionedSettingsAdmin):
    pass


@admin.register(HeroSettings)
class HeroSettingsAdmin(SectionedSettingsAdmin):
    pass


@admin.register(AboutSettings)
class AboutSettingsAdmin(SectionedSettingsAdmin):
    pass


@admin.register(LinksSettings)
class LinksSettingsAdmin(SectionedSettingsAdmin):
    pass


@admin.register(AddressSettings)
class AddressSettingsAdmin(SectionedSettingsAdmin):
    pass


@admin.register(CatalogSettings)
class CatalogSettingsAdmin(SectionedSettingsAdmin):
    pass


@admin.register(QuoteSettings)
class QuoteSettingsAdmin(SectionedSettingsAdmin):
    pass
