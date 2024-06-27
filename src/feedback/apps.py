from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig


class FeedbackConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'feedback'
    verbose_name = _("Feedback")
