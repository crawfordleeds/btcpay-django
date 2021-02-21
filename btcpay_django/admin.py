from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

from .models import BtcpayClient


class BtcpayClientAdmin(admin.ModelAdmin):

    list_display = (
        "pairing_code",
        "host",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "pairing_code",
                    "host",
                )
            },
        ),
    )
    search_fields = ("host",)


try:
    admin.site.register(BtcpayClient, BtcpayClientAdmin)
except AlreadyRegistered:
    pass
