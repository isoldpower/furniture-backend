from django.contrib import admin

from portfolio.models.portfolio_list import PortfolioItem


@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    pass
