import api.questions as questions

for ticker in questions.q2():
    symbol = ticker.get('symbol')
    spread = questions.q4(ticker)
    print("%s: spread: %f" % (symbol, spread))

