import pickle
from .models import BtcpayClient
from django.conf import settings


def get_btcpay_client(host=None):
    if not host:
        host = settings.DEFAULT_HOST
    client = BtcpayClient.objects.filter(host=host).order_by("-created_at").first()
    if not client:
        raise Exception(f"Missing BTCPay client for host {host}")
