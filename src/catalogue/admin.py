from django.contrib import admin

from catalogue.models.product_material import ProductMaterial
from catalogue.models.stock_product import StockProduct
from catalogue.models.stock_section import StockSection


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
    list_display = ["title", "paragraph", "href_postfix"]
