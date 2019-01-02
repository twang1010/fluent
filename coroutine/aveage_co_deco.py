"""
>>> ro = average_cor()
>>> from inspect import getgeneratorstate
>>> getgeneratorstate(ro)
'GEN_SUSPENDED'

>>> ro.send(10)
10.0

>>> ro.send(20)
15.0

>>> ro.send(30)
20.0

"""

from corutil import coroutine


@coroutine
def average_cor():
    sum = 0.0
    count = 0
    average = None
    while True:
        item = yield average
        sum += item
        count += 1
        average = sum / count
