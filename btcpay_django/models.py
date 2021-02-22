import pickle

from btcpay import BTCPayClient as BTCPayClient_sdk
from crawfish.models import BaseModel
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .app_settings import BTCPAYSERVER_HOST


class BtcpayClient(BaseModel):
    class Meta:
        verbose_name = "BTCPay Client"
        verbose_name_plural = "BTCPay Clients"

    client = models.BinaryField(_("Pickled Client"), blank=True)
    pairing_code = models.CharField(
        _("Pairing Code"), help_text="One time use pairing code", max_length=50
    )
    host = models.URLField()

    def save(self, *args, **kwargs):
        """
        Override the save method to create a new client when creating a new record.
        """
        created = self.pk is None

        if created:
            assert (
                self.pairing_code is not None
            ), "You must add a pairing_code to created a new BtcpayClient record"
            if not self.host:
                assert (
                    BTCPAYSERVER_HOST is not None
                ), "ADD BTCPAYSERVER_HOST to your settings or pass `host` to the save() method."
                client = BTCPayClient_sdk.create_client(
                    host=settings.BTCPAYSERVER_HOST, code=self.pairing_code
                )
            else:
                client = BTCPayClient_sdk.create_client(
                    host=self.host, code=self.pairing_code
                )

            self.client = pickle.dumps(client)
        super().save(*args, **kwargs)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"BtcpayClient(host: '{self.host}')"
