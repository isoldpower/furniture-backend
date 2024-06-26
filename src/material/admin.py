from django.contrib import admin

from material.models.detailed_material import DetailedMaterial


@admin.register(DetailedMaterial)
class DetailedMaterialAdmin(admin.ModelAdmin):
    list_display = ["title", "href_postfix", "important"]
    search_fields = ["title"]
    list_filter = ["important"]
