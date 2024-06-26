from django.contrib import admin

from image.models.doublesided_image import DoublesidedImage


@admin.register(DoublesidedImage)
class DoublesidedImageAdmin(admin.ModelAdmin):
    list_display = ["verbose_name", "src", "low_src"]
    fields = ["verbose_name", "src", "low_src", "alt"]
    search_fields = ["verbose_name"]
