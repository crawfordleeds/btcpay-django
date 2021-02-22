import pickle
from .models import BtcpayClient
from django.conf import settings
from importlib import import_module
from .app_settings import BTCPAYSERVER_HOST


def get_btcpay_client(host=None):
    host = host or BTCPAYSERVER_HOST
    assert (
        host
    ), f"Either set BTCPAYSERVER_HOST in your settings or pass `host` as argument to get_btcpay_client"
    client = BtcpayClient.objects.filter(host=host).order_by("-created_at").first()
    if not client:
        raise Exception(f"No BTCPay client available for host {host}")

    return pickle.loads(client.client)
