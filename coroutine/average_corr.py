def average_corr():
    sum = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        sum += term
        count += 1
        average =sum/count


acc = average_corr()
next(acc)
print(acc.send(10))
print(acc.send(20))
print(acc.send(30))
