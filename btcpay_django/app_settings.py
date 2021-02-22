from django.conf import settings

BTCPAYSERVER_HOST = getattr(settings, "BTCPAYSERVER_HOST", None)
