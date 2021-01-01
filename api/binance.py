import requests

ENDPOINT = "https://api.binance.com/api/v3"


def request(method, path):
    resp = requests.request(method, ENDPOINT + path)
    if resp.status_code == 200:
        data = resp.json()
        return data
    else:
        raise Exception(resp.status_code)


def statistic24():
    return request('GET', '/ticker/24hr')


def order_book(symbol, limit=500):
    return request('GET', '/depth?symbol=%s&limit=%s' % (symbol, limit))
