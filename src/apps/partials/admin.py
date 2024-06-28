from django.contrib import admin

from .models import FirmAdvantage, MaterialAdvantage, DoublesidedImage


@admin.register(FirmAdvantage)
class FirmAdvantageAdmin(admin.ModelAdmin):
    list_filter = ["id"]
    search_fields = ["title", "paragraph"]


@admin.register(MaterialAdvantage)
class MaterialAdvantageAdmin(admin.ModelAdmin):
    list_filter = ["id"]
    search_fields = ["title", "paragraph"]


@admin.register(DoublesidedImage)
class DoublesidedImageAdmin(admin.ModelAdmin):
    list_display = ["verbose_name", "src", "low_src"]
    fields = ["verbose_name", "src", "low_src", "alt"]
    search_fields = ["verbose_name"]

