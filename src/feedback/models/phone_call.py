from django.utils.translation import gettext_lazy as _
from django.db import models

from feedback.models.abstracts import CallRequest


class PhoneCallRequest(CallRequest):
    """Inheritor of CallRequest model representing a call request by phone number"""
    phone_number = models.CharField(max_length=31, unique=True, verbose_name=_("Phone number"))
    email_address = models.CharField(max_length=255, unique=True, verbose_name=_("Email address"))

    class Meta:
        verbose_name = _("Phone call")
        verbose_name_plural = _("Phone calls")
        db_table = "phone_calls"

    def __str__(self):
        return self.name + ' (' + self.phone_number + ')'
