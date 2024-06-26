from django.utils.translation import gettext_lazy as _
from django.db import models
import uuid

from catalogue.models.stock_product import StockProduct


class CallRequest(models.Model):
    """Model representing the request for future call or contact"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("Request id"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Creation date"))
    name = models.CharField(max_length=255, verbose_name=_("Client name"))
    product = models.ForeignKey(StockProduct, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=_("Product of interest"))

    class Meta:
        db_table = 'calls'
        abstract = True
