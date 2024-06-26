from django.contrib import admin

from section.models.detailed_section import DetailedSection


@admin.register(DetailedSection)
class DetailedSectionAdmin(admin.ModelAdmin):
    search_fields = ["title", "paragraph", "href_postfix"]
    list_display = ["title", "paragraph", "href_postfix"]
