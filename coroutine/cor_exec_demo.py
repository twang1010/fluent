class DemoException(Exception):
    pass


def demo_except_handling():
    print('->coroutine started')
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print('DemoException handled')
            else:
                print('received {!r}'.format(x))
    finally:
            print('->coroutine ended')
