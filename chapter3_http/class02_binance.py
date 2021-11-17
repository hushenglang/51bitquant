"""
this is Binance exchange http request client
"""
import requests
import json


class BinanceFutureHttp(object):
    def __init__(self, api_key, api_secret, base_url=None):
        if base_url is None:
            self._base_url = "https://api.binance.com"
        self._api_key = api_key
        self._api_secret = api_secret
        self._timeout = 5

    def ping_server(self):
        endpoint = "/api/v3/ping"
        url = self._base_url + endpoint
        response = requests.get(url, timeout=self._timeout).json()
        return response

    def server_time(self):
        endpoint = "/api/v3/time"
        url = self._base_url + endpoint
        response = requests.get(url, timeout=self._timeout).json()
        return response

    def get_klines(self, symbol, interval, startTime=None, endTime=None, limit=500):
        endpoint = "/api/v3/klines"
        url = self._base_url + endpoint
        params = {
            "symbol": symbol,
            "interval": interval,
            "limit": limit
        }
        if startTime is not None:
            params["startTime"] = startTime
        if endTime is not None:
            params["endTime"] = endTime
        response = requests.get(url, params, timeout=self._timeout).json()
        return response

    def get_tick_price(self, symbol):
        endpoint = "/api/v3/ticker/price"
        url = self._base_url + endpoint
        params = {
            "symbol": symbol
        }
        response = requests.get(url, params, timeout=self._timeout).json()
        return response


if __name__ == '__main__':
    api_key = ""
    api_secret = ""
    binanceClient = BinanceFutureHttp(api_key, api_secret)
    response = binanceClient.ping_server()
    print("ping: ", response)
    response = binanceClient.server_time()
    print("time: ", response)
    response = binanceClient.get_klines("BTCUSDT", "1m")
    print("klines: ", response)
    response = binanceClient.get_tick_price("BTCUSDT")
    print("ticker: ", response)
