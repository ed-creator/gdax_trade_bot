from django.db import models
import gdax


public_client = gdax.PublicClient()

#Class to model a ONE/TWO pair e.g. ETH/BTC market price ≈ 0.1
class TradingPair(models.Model):
    title = models.CharField(max_length=200)
    bid = models.FloatField()
    ask = models.FloatField()
    one_name = models.CharField(max_length=3)
    one_balance = models.FloatField()
    two_name = models.CharField(max_length=3)
    two_balance = models.FloatField()

    def add_trading_pair(self,one,two):
        self.title = (one + '-' + two)
        self.one_name = one
        self.two_name = two
        order_book = public_client.get_product_order_book(self.title)
        self.bid = order_book['bids'][0][0]
        self.ask = order_book['asks'][0][0]
