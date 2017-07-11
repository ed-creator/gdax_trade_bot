from django.db import models
import gdax


public_client = gdax.PublicClient()

class EthBtc(models.Model):
    product = models.CharField(max_length=200)
    ticker = models.CharField(
        max_length=3)
