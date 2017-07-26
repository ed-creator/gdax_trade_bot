import requests

wanted_coins = ['BTC','ETH','LTC']

def get_coin_list(tickers):
    
    r = requests.get('https://www.cryptocompare.com/api/data/coinlist/')
    return r.json()['Data']
