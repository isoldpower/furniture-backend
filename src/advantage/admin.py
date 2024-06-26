from django.contrib import admin

from advantage.models.specific_advantage import FirmAdvantage, MaterialAdvantage


@admin.register(FirmAdvantage)
class FirmAdvantageAdmin(admin.ModelAdmin):
    list_filter = ["id"]
    search_fields = ["title", "paragraph"]


@admin.register(MaterialAdvantage)
class MaterialAdvantageAdmin(admin.ModelAdmin):
    list_filter = ["id"]
    search_fields = ["title", "paragraph"]
