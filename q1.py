import api.questions as questions

for ticker in questions.q1():
    print("%s %s" % (ticker.get('symbol'), ticker.get('volume')))
