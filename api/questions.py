import re
from functools import reduce
import api.binance as binance

btc = re.compile(r'.+BTC')
usdt = re.compile(r'.+USDT')


def q1():
    stat = sorted(filter(lambda x: btc.match(x.get('symbol')), binance.statistic24()), key=lambda k: k['volume'],
                  reverse=True)[0:5]
    return stat


def q2():
    stat = sorted(filter(lambda x: usdt.match(x.get('symbol')), binance.statistic24()), key=lambda k: k['count'],
                  reverse=True)[0:5]
    return stat


def q3(ticker):
    symbol = ticker.get('symbol')
    order_book = binance.order_book(symbol)
    bids = reduce(lambda x, y: x + y, map(lambda x: float(x[0]) * float(x[1]), order_book.get('bids')[0:200]))
    asks = reduce(lambda x, y: x + y, map(lambda x: float(x[0]) * float(x[1]), order_book.get('asks')[0:200]))
    return bids, asks


def q4(ticker):
    symbol = ticker.get('symbol')
    order_book = binance.order_book(symbol)
    spread = float(order_book.get('asks')[0][0]) - float(order_book.get('bids')[0][0])
    return spread
