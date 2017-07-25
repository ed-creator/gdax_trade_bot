from django.db import models

# Create your models here.
class Coin(models.Model):
    name = models.CharField(max_length=200)
    ticker = models.CharField(max_length=6)
    btc_price = models.FloatField()
    usd_price = models.FloatField()
    eth_price = models.FloatField()
