import api.questions as questions

for ticker in questions.q2():
    print("%s %s" % (ticker.get('symbol'), ticker.get('count')))
