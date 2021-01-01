import time

import api.questions as questions

tickers = questions.q2()

prev = {}

try:
    while True:
        start = time.time()
        for ticker in tickers:
            symbol = ticker.get('symbol')
            spread = questions.q4(ticker)
            if symbol in prev.keys():
                print("%s: spread: %f (%f)" % (symbol, spread, spread - prev[symbol]))
            else:
                print("%s: spread: %f" % (symbol, spread))
            prev[symbol] = spread
        wait = 10 - (time.time() - start)
        print("---- waiting %f seconds" % wait)
        if wait > 0:
            time.sleep(wait)
except KeyboardInterrupt:
    print("Stopped")

