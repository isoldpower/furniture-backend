from django.contrib import admin

from product.models.detailed_product import DetailedProduct


@admin.register(DetailedProduct)
class DetailedProductAdmin(admin.ModelAdmin):
    list_display = ["title", "preparation_time", "estimated_cost", "href_postfix", "is_important"]
    list_filter = ["is_important"]
    search_fields = ["title", "href_postfix", "description"]
