from django.contrib import admin

from .models import ProductMaterial, StockSection, StockProduct


@admin.register(ProductMaterial)
class DetailedMaterialAdmin(admin.ModelAdmin):
    list_display = ["title", "href_postfix", "important"]
    search_fields = ["title"]
    list_filter = ["important"]


@admin.register(StockProduct)
class DetailedProductAdmin(admin.ModelAdmin):
    list_display = ["title", "preparation_time", "estimated_cost", "href_postfix", "important"]
    list_filter = ["important"]
    search_fields = ["title", "href_postfix", "description"]


@admin.register(StockSection)
class DetailedSectionAdmin(admin.ModelAdmin):
    search_fields = ["title", "paragraph", "href_postfix"]
    list_display = ["title", "href_postfix", "visible_in_header", "visible_in_preview"]
