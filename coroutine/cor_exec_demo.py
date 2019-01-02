class DemoException(Exception):
    pass


def demo_except_handling():
    print('->corutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('DemoException handled')
        else:
            print('received {!r}'.format(x))
    raise RuntimeError


corr = demo_except_handling()
next(corr)
corr.send(10)
corr.send(11)