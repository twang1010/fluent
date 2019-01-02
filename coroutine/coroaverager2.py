"""
>>> ave_cc = averager()
>>> next(ave_cc)
>>> ave_cc.send(10)
>>> ave_cc.send(20)
>>> ave_cc.send(30)
>>> try:
...     ave_cc.send(None)
... except StopIteration as ex:
...     result = ex.value
...
>>> result
Result(count=3, average=20.0)
"""

from collections import namedtuple

Result = namedtuple('Result', 'count average')


def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        item = yield
        if item is None:
            break
        total += item
        count += 1
        average = total/count
    return Result(count, average)
