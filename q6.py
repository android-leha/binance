import time
import api.questions as questions

from prometheus_client import start_http_server, Gauge

start_http_server(8080)

print("Check the metrics on http://localhost:8080/metrics")

tickers = questions.q2()
METRICS = {}
PREV_METRICS = {}
prev = {}

for ticker in tickers:
    symbol = ticker.get('symbol')
    METRICS[symbol] = Gauge("%s_spread" % symbol.lower(), "%s spread" % symbol)
    PREV_METRICS[symbol] = Gauge("%s_diff" % symbol.lower(), "%s spread diff" % symbol)
    prev[symbol] = float(0)

while True:
    start = time.time()
    for ticker in tickers:
        symbol = ticker.get('symbol')
        spread = questions.q4(ticker)
        METRICS[symbol].set(spread)
        diff = spread - prev[symbol]
        PREV_METRICS[symbol].set(diff)
        prev[symbol] = spread
        print("%s: spread: %f (%f)" % (symbol, spread, diff))
    wait = 30 - (time.time() - start)
    if wait > 0:
        time.sleep(wait)
