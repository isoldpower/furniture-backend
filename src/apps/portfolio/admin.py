from django.contrib import admin

from apps.portfolio.models.portfolio_item import PortfolioItem


@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    pass
