import time
from clock_deco2 import clock

@clock
def snooze(seconds):
    time.sleep(seconds)

@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)

if __name__=='__main__':
    print('*' * 40, 'calling snooze(.123)')
    snooze(.123)

    print('*' * 40, 'calling factorial(6)')
    print('6! =' , factorial(6))
    # function name and dir were blind by decorator, using function.wraps will solve this issue
    print(factorial.__name__, factorial.__doc__)
