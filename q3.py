import api.questions as questions

for ticker in questions.q1():
    symbol = ticker.get('symbol')
    (bids, asks) = questions.q3(ticker)
    print("%s: bids: %f, asks: %f" % (symbol, bids, asks))

