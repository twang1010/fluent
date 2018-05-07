import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'


def clock(fmt=DEFAULT_FMT):
    def deco(func):
        def clocked(*_args):
            t0 = time.perf_counter()
            _result = func(*_args)
            elapsed = time.perf_counter() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            #if not fmt:
            print(fmt.format(**locals()))
            #else:
            #    print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
            return _result
        return clocked
    return deco

if __name__ == '__main__':
    print('=======default fmt parameters ======')
    @clock()
    def snooze(seconds):
        time.sleep(seconds)

    for i in range(3):
        snooze(.123)

    print('=======customized fmt parameters ======')
    @clock('{name}: {elapsed}s')
    def snooze1(seconds):
        time.sleep(seconds)

    for i in range(3):
        snooze1(.123)