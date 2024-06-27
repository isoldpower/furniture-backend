from django.contrib import admin

from feedback.models.phone_call import PhoneCallRequest


class PhoneCallRequestInline(admin.TabularInline):
    model = PhoneCallRequest


@admin.register(PhoneCallRequest)
class PhoneCallRequestAdmin(admin.ModelAdmin):
    list_display = ["name", "phone_number", "email_address", "product"]
    search_fields = ["name", "phone_number", "email_address", "product"]
    list_filter = ["created_at"]
