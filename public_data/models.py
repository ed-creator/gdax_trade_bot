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

    def create_trading_pair(cls,one,two):
        cls.title = (one + '-' + two)
        cls.one_name = one
        cls.two_name = two
        cls.update_pair_state()
        return cls


    def update_pair_state(cls):
        order_book = public_client.get_product_order_book(cls.title)
        cls.bid = order_book['bids'][0][0]
        cls.ask = order_book['asks'][0][0]
